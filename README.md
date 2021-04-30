# set-cover-np-completeness
a python implementation of the set cover problem, and a proof of np-completeness with a reduction from the vertex-cover problem in polynomial time.

to run the algorithm, clone this repository and run:
`python main.py` or `python3 main.py`, depending on which python compiler you have.
  acceptable flags:
    `-l`, `--log`, for runtime logs 

also, if you're interested, check out `reduction.py`. This file consists on a polynomial time reduction of a instance of the vertex-cover problem. A reduction for decision problems consists on receiving a valid instance of the source problem, execute some work algorithmicly to adapt the input to become a valid instance of another problem which you previously solved, execute the algorithm using the adapted input and then solve the original problem with the given output. For more info, read the pdf, which unfortunately is available only in portuguese.
