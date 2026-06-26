import pickle
import copy

class PickleDumper:

    def __init__(self, *classes, dump=False, home="pd"):
        self.names = {}
        self.dumpers = []
        self.home = home
        if dump is True:
            self.dumps(*classes, home=home)

    def __str__(self):
        return f"Pickle Dumper\nDumps classes number: {len(self.dumpers)}"
    
    def dumps(self, *classes, home="pd"):
        for cs in classes:
            name = cs.__class__.__name__
            if name in self.names:
                self.names[name] += 1
                count = f"_{self.names[name]}.pkl"

                with open(name + count, "wb") as f:
                    pickle.dump(cs, f)
                self.dumpers.append(name + count)
            else:
                self.names[name] = 1
                count = f"_{self.names[name]}.pkl"
                with open(name + count, "wb") as f:
                    pickle.dump(cs, f)
                self.dumpers.append(name + count)
        if self.home is not False:
            pd = copy.deepcopy(self)
            with open(home + ".pkl", "wb") as f:
                pickle.dump(pd, f)

    def parent_dumps(self, parent ,home="pd"):
        
        self.fields = tuple(vars(parent).keys())
        for name, field in vars(parent).items():
            if field is self:
                continue
            
            with open(name + ".pkl", "wb") as f:
                pickle.dump(field, f)
            self.dumpers.append(name + ".pkl")
            
        if self.home is not False:
            pd = copy.deepcopy(self)
            with open(home + ".pkl", "wb") as f:
                pickle.dump(pd, f)

    def parent_back(self=None, parent=None, home="pd"):
        if home is not False:
            with open(home, "rb") as f:
                pd = pickle.load(f)
            fields = pd.fields
            values = pd.comeback(home=home)
        else:
            fields = self.fields
            values = self.comeback()
        for fi, val in zip(fields, values):
            setattr(parent, fi, val)
    
    def comeback(self=None, *addings, home="pd"):
        if home is not False:
            with open(home, "rb") as f:
                pd = pickle.load(f)
            dumpers = pd.dumpers
            names = pd.names
        else:
            dumpers = self.dumpers
            names = self.names
        backs = []
        for d in dumpers:
            with open(d, "rb") as f:
                backs.append(pickle.load(f))
        if addings != ():
            for a in addings:
                with open(a, "rb") as f:
                    backs.append(pickle.load(f))
        if home is not False:
            return pd, backs
        else:
            return backs
