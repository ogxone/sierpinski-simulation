<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Sierpinski_triangle.svg/220px-Sierpinski_triangle.svg.png" alt="drawing" width="200"/>

# Sierpinski fractal drawing simulation

Visualization of the process of drawing of sierpinski triangle

## Installing / Getting started


```shell
python3 -m pip install -r requirement.txt
```

The only required package for now is turtle

### Run

Run the simulation with the following command

```shell
python3 -m runner
```

## Configuration

Below is a list of available options

#### depth
Type: `int`  
Default: `2`

Nesting level

Example:
```bash
python3 -m runner --depth=5  # Will draw the triangle with nesting level 5
```
