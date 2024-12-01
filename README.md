# Embodied AI demo

## env formulation
In the eval code, we set 4 actions as **goto**, **pick up**, **place** and **done**, you can follow action list in eval list to execute actions.

* detail instructions follow:[gazebo-sim-env](https://github.com/RLC-Lab/Simulation-For-Embodied-AI/blob/main/sim_robot.md)

* navigation points:
fruit table     0.610712 5.894910
drink table     6.96548 -4.40075
toy table   -6.83587 -4.10468
shipping table(NULL)    7.65881 5.69058
receving shelf      -4.66216 3.40295


## project architecture
```
.
├── arm_eval_pose.py
├── checkpoints
│   ├── checkpoint_detection.tar
│   ├── checkpoint_tracking.tar
│   ├── GroundingDINO_SwinB.cfg.py
│   ├── groundingdino_swinb_cogcoor.pth
│   └── sam_vit_h_4b8939.pth
├── distance_calculator.py
├── example_data
├── executor_a.py
├── executor.py
├── grasping.py
├── grasp_utils.py
├── image.py
├── images
├── init_detect_arm.py
├── license
│   ├── licenseCfg.json
│   ├── ZixuanWang.lic
│   ├── ZixuanWang.public_key
│   └── ZixuanWang.signature
├── main.py
├── mindistance.py
├── my_report.nsys-rep
├── navigation.py
├── __pycache__
├── README.md
└── test_camera_convert.py
```
* In `executor_a.py` file, we setup the computing pipeline
* In `navigation.py` file, we send target pose to move_base and navigate
* In `grasping.py` file, we define grasping functions
* In `distance_calculator.py` file, we compute the navigation distance.
* In `./example_data`, we save pics duiring grasping

## run eval codes

* Prompt reference:[prompt](https://docs.google.com/spreadsheets/d/1UrIG7LHF4WJM_hiuAmXeE8Dqxm40UvmpL2OosR3onaI/edit?gid=1467546178#gid=1467546178)

* Firstly, init the arm pose:
```shell
conda activate grasp-env
python init_detect_arm.py
```
* Meanwhile, prepare grasping init:
```shell
conda activate grasp-env
python test_camera_convert
```
* Then, run the pipeline manually:
```shell
conda activate grasp-env
python executor_a.py
```
during this processing, user need to input the target postion  
```
action_type(1_navi 2_pick 3_place 4_done): 
1(manually choose)
param: -4.66216 3.40295
goto[table][-4.66216 3.40295]
navigatoin
goto[table][-4.66216 3.40295]
-4.66216 3.40295
move_base:  ['-4.66216', '3.40295']
```

* deal with navigation planning error:
```shell
rosparam set use_sim_time true
```