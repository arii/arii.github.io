# Portfolio Migration Plan

This document outlines the content and media from the legacy repository (`arii.github.io`) that should be ported to the new portfolio repository (`arii/portfolio`) to enrich the `/research` or `/devai` pages.

## 1. Images for Autonomous Tools (`src/data/research/autonomousTools.ts`)

The new portfolio lists several autonomous and research tools, but many are lacking corresponding media that exist in the legacy repository's `img/` directory.

| Project ID in Portfolio | Corresponding Legacy Project | Image to Port |
| --- | --- | --- |
| `boop-light-detector` | Boop Light Detector | `img/app_testing.jpg` |
| `light-therapy-mit` | Light Therapy at MIT | `img/light.jpg` |
| `bwsi-racecar` | BeaverWorks Summer Institute | `img/bw.jpg` |
| `delivery-bots` | Delivery Bots | `img/beer.png` (or `img/beer_bot.jpg`) |
| `robocon-mit` | RoboCon MIT | `img/robocon.jpg` |
| `autonomous-drone-line-following` | Drone Line Following Project | `img/drone.jpg` |
| `swag-grasping` | Learning SWAG | `img/thesis_wordle.png` (and `img/swag.jpg`) |
| `leac-monitoring-software` | Lab Energy Assessment Center (LEAC) | `img/leac.jpg` |
| `cad-cam-dental-workflow` | CAD/CAM Robotic Dental Crowning Workflow | `img/dental.jpg` |

## 2. Media for PhD Research (`src/data/research/flagshipTools.ts`)

The new portfolio features the PhD Thesis as a flagship tool (`phd-thesis`) and already references `sixblock.png`. However, the legacy repository contains additional rich media that can be used to further enhance the PhD thesis section or create a dedicated case study page.

**Images (`phd/` directory):**
- `phd/placing.png`
- `phd/tetris1.png`
- `phd/tetris2.png`
- `phd/tetris3.png`
- `phd/beliefoverlay.png`

**Videos (`phd/` directory):**
- `phd/placing.mp4`
- `phd/sixblock.mp4`
- `phd/tetris1.avi`
- `phd/tetris2.avi`
- `phd/tetris3.avi`
- `phd/beliefoverlay.avi`

**Documents:**
- `phd/thesis.pdf` (Can be linked or hosted directly instead of relying on DSpace alone)

## 3. Reports for Academic / Research Projects (`reports/` directory)

Several PDF reports in the legacy repository correspond to projects or past research and could be added as downloadable assets or linked from project cards:
- `reports/report_dental.pdf` (Relevant for `cad-cam-dental-workflow`)
- `reports/report_ml.pdf` (Could be relevant for general DevAI or machine learning projects)
- `reports/report_6375.pdf`
- `reports/report_ce118.pdf`
- `reports/report_ce121.pdf`

## 4. Text Content

- The detailed project descriptions in `projects.md` and `phd.md` can be used to expand the short descriptions currently present in `autonomousTools.ts` and `flagshipTools.ts` into full Markdown files under `src/content/research/` in the new repository.

## 5. Other Potential Content

Some images in `img/` could be used for the `/about` or general overview pages if not already ported:
- `img/intro-pic.jpg`
- `img/grad.jpg`
- `img/csail_research.jpg`
- `img/csail.jpg`
- `img/rss.jpg`
