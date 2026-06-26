# PickleDumper
Custom smart self-sufficient loader for fast loading

# Mini instruction to use:
  The home parameter addects the saving and unloading of PickleDumper
  himself
  # init:
    p = PickleDumper(*classes, dump, home)
    dump = True / False - if you specify True, then *classes are saved, purely.
     home parameter is transferred to it.
    if you specify False, as instance of the class is simply created, without any saving.

  # dumps:.
    p.dumps(*classes, home)
    *classes - what needs to be saved.
    Dumper finds the names of each class, checks if they existed before and assigns them indexes.
    
  You'll see files likes this: class_index.pkl
    
    if you specifed home not False, but a real name like "pd",
    then it will also save itself in a file the name that you
    specifed in home.

  # comeback:
    p, backs = PickleDumper.comeback(*addings, home)
    When dumping, Dumper remembers everything and when you pass 
    the name of the file it saved itself to in home, it will instantly
    remember and return a list of backs.
    *addings - if you need to unload something extra

  # parent_dumps:
    p.parent_dumps(parent, home)
    with home, the same as in dumps.
    Dumper remembers the parent, accesses all its fields, remembers
    them and their values, and saves the field values.
  # parent_back:
    p.parent_back(parent, home)
    When dumping, Dumper remembers everything and when you pass 
    the name home, it will reterieve everything, remember all the
    classes and change the parent fields to the saved ones you passed.
    uses the comeback function.
# Good code!
