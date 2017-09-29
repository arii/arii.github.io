import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def simple_world():
    import create_planar_world
    reload(create_planar_world)

    from create_planar_world import GuiB2D
    from create_planar_world import createPlanarWorld

    # Start the gui
    screen_size = (640, 480)
    sim_size = (32, 24)
    fps = 60
    time_step = 1.0/fps
    gui = GuiB2D(screen_size, sim_size, fps) 
    gui.start()

    # Create a line juggling world
    world, bodies = createPlanarWorld(gravity=9.81)
    return world, bodies, gui, time_step


def run_pd_control(robot_pose=None, controller=None):
    world, bodies, gui, time_step = simple_world()
    robot = bodies['robot']

    if robot_pose is not None:
        x,y,th = robot_pose
        robot.position= (x,y)
        robot.angle = th
    else:
        # set robot position to middle of screen
        robot.position= (16, 12)
        robot.angle = 0


    
    # create arrays to hold the state and time values
    states = []
    times = []

    t= 0

    # run the simulation
    while gui.running:

        world.Step(time_step, 10, 10)
        gui.draw(world)
        t+= time_step

        # access current state info
        x,y = robot.position
        th = robot.angle
        vx,vy = robot.linearVelocity
        vth = robot.angularVelocity
        state = [x,y,th,vx,vy,vth]
        
        if controller is not None:
            u_x, u_y, u_th = controller(t, state)
            force = (u_x, u_y)
            robot.ApplyForceToCenter(force, True)
            robot.ApplyTorque(u_th, True)

        states.append(state)
        times.append(t)
    #close the window (doesn't work in mac)
    gui.stop()
    states = np.array(states)
    times = np.array(times)

    return [times, states]

def pd_control(robot, desired_pose, desired_vel):
    def closedLoopController (time, robot_state):
        
        K_px = 100
        K_py = 100
        K_pth = 10
        K_dx = 50
        K_dy = 50
        K_dth = 20

        # the output signal
        x,y,th, xdot, ydot, thdot = robot_state
        
        # the reference signal
        rx, ry, rth = desired_pose 
        rxdot, rydot, rthdot = desired_vel
        
        # the error signal
        e_x = rx - x
        e_y = ry - y
        e_th = rth - th

        e_xdot = rxdot - xdot
        e_ydot = rydot - ydot
        e_thdot = rthdot - thdot
        
        
        # the controller output
        u_x = K_px*e_x + K_dx*e_xdot
        u_y = K_py*e_y + K_dy*e_ydot
        u_th = K_pth*e_th + K_dth*e_thdot
        
        return u_x, u_y, u_th 
    
    # access current state info
    x,y = robot.position
    th = robot.angle
    vx,vy = robot.linearVelocity
    vth = robot.angularVelocity
    state = [x,y,th,vx,vy,vth]
    
    u_x, u_y, u_th = closedLoopController(0, state)
    force = (u_x, u_y)
    robot.ApplyForceToCenter(force, True)
    robot.ApplyTorque(u_th, True)



def plot(result, body_name):
    times, states = result
    labels = [
            ("horizontal position", "meters", "time(s)"),
            ("vertical position", "meters", "time(s)"),
            ("angular position", "radians", "time(s)"),
            ("horizontal velocity", "meters/sec", "time(s)"),
            ("vertical velocity", "meters/sec", "time(s)"),
            ("angular velocity", "radians/sec", "time(s)"),
            ]


    rows = 2
    cols = 3

    plt.close()
    f, arr = plt.subplots(rows, cols, sharex='col')
    for r in range(rows):
        for c in range(cols):
            ax = arr[r,c]
            index = r*cols + c
            title, ylabel, xlabel = labels[index]
            ax.plot(times, states[:,index])
            ax.set_title(title)
            ax.set_ylabel(ylabel)
            ax.set_xlabel(xlabel)

            ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
            ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

    plt.suptitle("%s state information versus time" %body_name)
    f.set_figheight(6)
    f.set_figwidth(10)
    f.subplots_adjust(hspace=.8, wspace=1, top=.8)
    plt.show()



def analytical_bounce(y0, ydot0, e, t_final):

    def compute_bounce(a,b,c):
        t_f_1= (-b + (b**2 - 4*a*(c-1.5))**0.5)/(2*a)
        t_f_2= (-b - (b**2 - 4*a*(c-1.5))**0.5)/(2*a)
        t_f = max(t_f_1, t_f_2)
        T = np.linspace(0, t_f).tolist()
        y = [c + b*t + a*t**2 for t in T]
        ydot = [b + 2*a*t for t in T]

        return y, ydot, T
    
    a = 0.5*-9.81
    b = ydot0 
    c = y0 
    y,ydot, T = compute_bounce(a,b,c)
    
    if e == 0:
        if t_final < T[-1]:
            return y, T
        else:
            y+= [y[-1]]
            T += [t_final]
        return y, T
    bounces = 0
    while T[-1] < t_final:
        
        b = e*-ydot[-1] 
        c = y[-1]
        next_y, next_ydot, next_T = compute_bounce(a,b,c)
        y += next_y
        ydot += next_ydot
        T += [t + T[-1] for t in next_T]
        bounces += 1
        if bounces > 20: break
    return y, T

def plot_analytical_vs_sim(result, restitution):


    # plot analytical equation versus simulated results
    T_sim, y_sim = result[0], result[1][:,1]

    y0 = y_sim[0]
    ydot0 = 0
    t_final = T_sim[-1]
    y_an, T_an = analytical_bounce(y0, ydot0, restitution, t_final)
    plt.close()
    plt.plot(T_an, y_an, label="analytical")
    plt.plot(T_sim, y_sim, label="simulated")
    plt.legend()
    plt.title("Analytical versus Simulated Position")
    plt.xlabel("time (s)")
    plt.ylabel("vertical height (m)")
    plt.show()


def get_state(body):
    # access current state info
    x,y = body.position
    th = body.angle
    vx,vy = body.linearVelocity
    vth = body.angularVelocity
    state = [x,y,th,vx,vy,vth]
    return state
        



def closedLoopController (time, robot_state, desired_pose, desired_vel):
    """
    The closed loop pd-controller for the robot paddle implemented
    in the previous section.
    """
    
    K_px = 100
    K_py = 100
    K_pth = 10
    K_dx = 50
    K_dy = 50
    K_dth = 20

    
    # the output signal
    x,y,th, xdot, ydot, thdot = robot_state
    
    # the reference signal
    rx, ry, rth = desired_pose 
    rxdot, rydot, rthdot = desired_vel
    
    # the error signal
    e_x = rx - x
    e_y = ry - y
    e_th = rth - th

    e_xdot = rxdot - xdot
    e_ydot = rydot - ydot
    e_thdot = rthdot - thdot
    
    # the controller output
    u_x = K_px*e_x + K_dx*e_xdot
    u_y = K_py*e_y + K_dy*e_ydot
    u_th = K_pth*e_th + K_dth*e_thdot
    
    return u_x, u_y, u_th 



def run_ball_dynamics( ball_pose=None, robot_pose=None, ball_controller=None, robot_controller=None, restitution=None, impact_goal=None, peak_goal=None):
    world, bodies, gui, time_step = simple_world()
    ball = bodies['ball']
    robot = bodies['robot']

    if peak_goal is not None:
        bodies['boundsU'].position = (30, peak_goal)

    if impact_goal is not None:
        bodies['boundsL'].position = (30, impact_goal)

    if restitution is not None:
        # make all bodies in contact have bounce collisions:
        ball.fixtures[0].restitution = restitution
        #bodies['ground'].restitution = restitution
        #robot.restitution = restitution



    if ball_pose is not None:
        x,y,th = ball_pose
        ball.position= (x,y)
        ball.angle = th
    else:
        # set ball position to top middle of screen
        ball.position= (16, 20)
        ball.angle = 0

    if robot_pose is not None:
        x,y,th = robot_pose
        robot.position= (x,y)
        robot.angle = th
    else:
        print "moving robot far away"
        # set robot out of screen
        robot.position= (100, 100)
        robot.angle = 0


    
    # create arrays to hold the state and time values
    robot_states = []
    ball_states = []
    times = []
    t= 0

    # run the simulation
    while gui.running:


        # access current state info
        ball_state = get_state(ball)
        robot_state = get_state(robot)

                
        if ball_controller is not None:
            u_x, u_y, u_th =ball_controller(t, ball_state)
            force = (u_x, u_y)
            com = ball.worldCenter 
            ball.ApplyLinearImpulse(force, point=com, wake=True)
            ball.ApplyAngularImpulse(u_th, True)
        
        if robot_controller is not None:
            u_x, u_y, u_th = robot_controller(t, robot_state, ball_state)
            force = (u_x, u_y)
            robot.ApplyForceToCenter(force, True)
            robot.ApplyTorque(u_th, True)

        world.Step(time_step, 10, 10)
        gui.draw(world)
        
        t+= time_step
        ball_states.append(ball_state)
        robot_states.append(robot_state)
        times.append(t)

    gui.stop()
    ball_states = np.array(ball_states)
    robot_states = np.array(robot_states)
    times = np.array(times)

    if robot_pose is None:
        return [times, ball_states]
    else:
        return [times, ball_states, robot_states]

def play_pd_control_solution(initial_pose, desired_pose, desired_vel):

    K_px = 100
    K_py = 100
    K_pth = 10
    K_dx = 50
    K_dy = 50
    K_dth = 20

    def closedLoopController (time, robot_state):
	
	# the output signal
	x,y,th, xdot, ydot, thdot = robot_state
	
	# the reference signal
	rx, ry, rth = desired_pose 
	rxdot, rydot, rthdot = desired_vel
	
	# the error signal
	e_x = rx - x
	e_y = ry - y
	e_th = rth - th

	e_xdot = rxdot - xdot
	e_ydot = rydot - ydot
	e_thdot = rthdot - thdot
	
	
	# the controller output
	u_x = K_px*e_x + K_dx*e_xdot
	u_y = K_py*e_y + K_dy*e_ydot
	u_th = K_pth*e_th + K_dth*e_thdot
	
	return u_x, u_y, u_th 

    result = run_pd_control(initial_pose, closedLoopController)

def play_full_solution():
    def vertical_energy(b_y, b_ydot):
	return 0.5*b_ydot**2 + 9.81*b_y


    ball_pose = (16, 20, 0)
    C = .5 # restitution
    impact_height = 10
    peak_height = 20

    cx = ball_pose[0]
    cy = impact_height
    robot_pose = (16, impact_height, 0)

    k_e = .005
    k_c = (1-C)/(1+C)

    n_d = vertical_energy(peak_height-impact_height, 0)


    def robot_controller(time, robot_state, ball_state):
	"""
	A catching controller.  The robot mirrors the movement
	of the ball.
	"""
	bx,by,bth,bxdot,bydot,bthdot = ball_state
	
	n_curr = vertical_energy(by-cy, bydot)
	
	kw = k_c + k_e*(n_d - n_curr)

	rx = cx + (bx - cx)
	ry = cy - kw*(by - cy)
	rth = 0
	rxdot = 0
	rydot = -kw*bydot
	rthdot = 0
	desired_pose = (rx, ry, rth)
	desired_vel = (rxdot, rydot, rthdot)
	return closedLoopController(time, robot_state, desired_pose, desired_vel)
	
	

    result = run_ball_dynamics(ball_pose=ball_pose,  \
			       robot_pose = robot_pose, \
			       restitution=C, \
			       robot_controller=robot_controller, \
			       peak_goal = peak_height, \
			       impact_goal = impact_height)



