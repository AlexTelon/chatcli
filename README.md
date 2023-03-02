# cligpt

*Sample code only dont trust it!*

You need to provide your own API key. Ask chatGPT for how to do that and if you need provide the full openai_utils.py to it and ask what you should do.

*Sample code only dont trust it!*


```shell
What do you to do:find all python files and sum the nonempty lines
> find . -name "*.py" -exec wc -l {} \; | awk '{s+=$1} END {print s}'
Do you want to run this command or edit it? [y/n/e] 
```

```shell
> git config --global user.name "New Author"
Do you want to run this command or edit it? [y/n/e] 
```



The options are:

* y - yes run it. 

* n - no dont run it
   here you may give a change request basically and have it generate new suggestions. It will get the previous context.

* e - explain the suggestions. It will try to explain what the command means.


## Known issues

Running commands through the tools (choosing option y) is far from perfect. For instance the first example above does not run due to some issue with {} I think.

And again dont trust it. The AI may misunderstand you or generate suggestions for commands that may bork your computer. So as always be wary of commands suggested from the internet.

*Sample code only dont trust it!*