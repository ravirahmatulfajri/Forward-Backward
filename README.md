# Forward-Backward
Simple implementation of the forward-backward algorithm for TDT4171: Methods in AI

The Forward-Backward algorithm consists of two parts, the forward algorithm used for filtering, a process to recursively compute the joint probability of P(x<sub>t</sub>, y<sub>1:t</sub>) and
the backward algorithm used for smoothing, a process that moves backwards to edit the probabilities to more accurate values.

The setting is as follows; a man sits in a bunker, unable to observe the outsiden world. He is curious as to whether or not it is raining outside.
His only information about the world is seeing his boss, who is fortunate enough to not live in  the bunker, carry or not carry an umbrella.

If it is raining, there is a 90% chance his boss has an umbrella with him, if it is not raining there is a 20% chance he is carrying an umbrella. There is also a 70% chance of the weather being identical as the day before.

Given 50-50 odds the first day.


Part a):
The unobservable variable is the weather, or to be more precise, whether or not it is raining.

The observable variable is whether or not the protagonists boss has an ubrella.

The dynamic/transitional model is presented as matrices in the code.


The assumptions in this model are for that both rain and not rain are equally likely at the initial state, which is not necessarily true. Further one could argue that this is very simplified view of how weather operates in the real world. The model assumes constant transitional matrices as well as a very predictable boss.