# Pico utils

Pico is a two instruction bf minimisation with somewhat complex semantics for each of its two symbols
<code>[</code>, <code>]</code>
The first symbol represents a call to a function that takes a variable number of copies of itself as arguments.

This repo consists of two transducer programs:

* pico2python
* bf2pico

Written in four different languages:

* shell script: [pico2python.sh](pico2python.sh) | [bf2pico.sh](bf2pico.sh)
* bf: [pico2python.bf](pico2python.bf) | [bf2pico.bf] *PENDING* 
* pico: [pico2python.pico](pico2python.pico) | [bf2pico.pico] *PENDING*
* python: [pico2python.py](pico2python.py) | [bf2pico.py] *PENDING*

It also includes:

* [pico.sh](pico.sh) : A standalone bash shell pico interpreter which uses Python to execute the transduced pico code.


### Examples

Transduce and run a bf program:

    ./bf2pico.sh examples/hw.bf | ./pico.sh


Transduce and run a bf self interpreter (dbfi.b), with input hw.bf:

    python <(./bf2pico.sh examples/dbfi.b | ./pico2python.sh ) < <(echo -e "$(sed 's/\(.\)/\1\n/g' examples/hw.bf)\n!")

or

    echo -e "$(sed 's/\(.\)/\1\n/g' examples/hw.bf)\n!" |  ./pico.sh <(./bf2pico.sh examples/dbfi.b)

or

    ./pico.sh <(./bf2pico.sh examples/dbfi.b) < <(echo -e "$(fold -w1 examples/hw.bf)\n!" )
    
or    

    ./pico.sh <(./bf2pico.sh examples/dbfi.b) < <(echo -e ",[,.]\!It's a cat program" | fold -w1 )


### Experimenting with transducing pico2python.pico into Python using itself as the transducer:

    ./pico2python.py < <(echo -e "$(fold -w1 pico2python.pico)\n")

    ./pico.sh pico2python.pico < <(echo -e "$(fold -w1 pico2python.pico)\n")


**TODO:** Having the prompt `>` mixed in with the output is a problem. Find a neater solution for accepting input.
