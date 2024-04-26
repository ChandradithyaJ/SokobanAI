# SokobanAI

A Sokoban AI solver using the [gym-sokoban](https://github.com/mpSchrader/gym-sokoban) environment. Uses the reward values from the gym-sokoban environment to compute edge weights. The Branch and Bound algorithm was employed.

| Example Game 1 | Example Game 2 | Example Game 3 |
| :---: | :---: | :---: 
| ![Game 1](/docs/Animations/solved_3.gif?raw=true) | ![Game 2](/docs/Animations/solved_4.gif?raw=true) | ![Game 3](/docs/Animations/solved_5.gif?raw=true) |


### Via PIP
```bash
pip install gym-sokoban
```

### From Repository
```bash
git clone git@github.com:mpSchrader/gym-sokoban.git
cd gym-sokoban
pip install -e .
```
#### Room Variations
The available room configurations are shown in the table below. 

| Room Id | Grid-Size | Pixels | #Boxes | Example | TinyWorld |
| --- | :---: | :---: | :---: | :---: | :---: |
| Sokoban-v0 | 10x10 | 160x160 | 3 | ![Sokoban-v0](/docs/rooms/Sokoban-v0.png)  | ![Sokoban-v0](/docs/rooms/Tiny_World_Sokoban-v0.png) | 
| Sokoban-v1 | 10x10 | 160x160 | 4 | ![Sokoban-v1](/docs/rooms/Sokoban-v1.png) | ![Sokoban-v1](/docs/rooms/Tiny_World_Sokoban-v1.png) |
| Sokoban-v2 | 10x10 | 160x160 | 5 | ![Sokoban-v2](/docs/rooms/Sokoban-v2.png) | ![Sokoban-v2](/docs/rooms/Tiny_World_Sokoban-v2.png) |
| Sokoban-small-v0 | 7x7 | 112x112 | 2 |  ![Sokoban-small-v0](/docs/rooms/Sokoban-small-v0.png) | ![Sokoban-small-v0](/docs/rooms/Tiny_World_Sokoban-small-v0.png) |
| Sokoban-small-v1 | 7x7 | 112x112 | 3 | ![Sokoban-small-v1](/docs/rooms/Sokoban-small-v1.png) | ![Sokoban-small-v1](/docs/rooms/Tiny_World_Sokoban-small-v1.png) |
| Sokoban-large-v0 | 13x11 | 208x176 | 3 | ![Sokoban-large-v0](/docs/rooms/Sokoban-large-v0.png) | ![Sokoban-large-v0](/docs/rooms/Tiny_World_Sokoban-large-v0.png) |
| Sokoban-large-v1 | 13x11 | 208x176 | 4 | ![Sokoban-large-v1](/docs/rooms/Sokoban-large-v1.png) |  ![Sokoban-large-v1](/docs/rooms/Tiny_World_Sokoban-large-v1.png) |
| Sokoban-large-v2 | 13x11 | 208x176 | 5 | ![Sokoban-large-v2](/docs/rooms/Sokoban-large-v2.png) | ![Sokoban-large-v2](/docs/rooms/Tiny_World_Sokoban-large-v2.png) | 
| Sokoban-huge-v0 | 13x13 | 208x208 | 5 | ![Sokoban-huge-v0](/docs/rooms/Sokoban-huge-v0.png) | ![Sokoban-huge-v0](/docs/rooms/Tiny_World_Sokoban-huge-v0.png)

Please note that the larger rooms might take some time to be created, especially on a laptop.

Choose any of these and import the corresponding version in the ```sokobanAI/sokobanAI.py``` file.

### Execute

Run ```sokobanAI/sokobanAI.py```, sit back and enjoy!
