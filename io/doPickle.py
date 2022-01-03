import pickle;

d=dict(name='KeyXK',age=19,score=57);
data=pickle.dumps(d);
print(data);

reborn = pickle.loads(data);
print(reborn);