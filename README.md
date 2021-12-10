# Loading

loading.py is an extremely minimal python package that allows for you to get those cool animated loading
texts you see in terminal applications

![loading gif](/img/load.gif)

##### tutorial

this package doesn't require a vast amount of explaining to learn how to use it. Here's an example
python script:

```python
from load_animate import Loading

if __name__ == '__main__':
    load = Loading() #creates a load instance
    load.start("loading stuff ") #starts displaying the loading terminal to the terminal
    time.sleep(5) #wait 5 seconds
    load.stop() #stop displaying the loading animation to the terminal
```

loading.py uses multiprocessing to allow you to load and process chunks of data whilst showing this cool animation to the user.
