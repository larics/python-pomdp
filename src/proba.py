import xml.etree.ElementTree as ET
import numpy as np
import funcs_matrix

e=ET.parse('../examples/Tiger.pomdpx').getroot()
tree = ET.parse('../examples/functional_imitation.pomdpx')
root = tree.getroot()



class klasa1:
	 def __init__(self,description,discount,states,actions,observations):
            self.description = description
            self.discount = discount
            self.states = states
            self.actions = actions
            self.observations = observations

listaVar=[]

for child in root:
        if child.tag == 'Description':
            description = child.text
        elif child.tag == 'Discount':
            discount = float(child.text)
for child in root.findall('Variable'):
        states=[]
        actions=[]
        observations=[]
        lista_nova=[]
        for k in child:
            for m in k:
                if m.tag == 'ValueEnum':
                    pom = m.text.split(' ')
                    if k.tag == 'StateVar':
                        states += pom
                    elif k.tag == 'ActionVar':
                        actions=pom
                    elif k.tag == 'ObsVar':
                        observations=pom

                elif m.tag == 'NumValue':
                    for t in range(1,int(m.text)+1):
                        if k.tag == 'StateVar':
                            states.append('s%s'%t)
                        elif k.tag == 'ActionVar':
                            actions.append('s%s'%t)
                        elif k.tag == 'ObsVar':
                            observations.append('s%s'%t)


        objekt = klasa1(description, discount, states, actions, observations)
        listaVar.append(objekt)

print(listaVar[0].states)
print(listaVar[0].observations)
print(listaVar[0].actions)


for k in root.findall('InitialStateBelief'):
       IsbList=[]
       for m in k.findall('CondProb'):
           for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    for p in o.findall('ProbTable'):
                        pom1=p.text.split(' ')
                        for x in pom1:
                            IsbList.append(float(x))
                            IsbVector=np.array(IsbList)

print(IsbVector)

StateTransitionDictionary = funcs_matrix.getMatrix('StateTransitionFunction', root)
ObservationFunctionDictionary = funcs_matrix.getMatrix('ObsFunction', root)

print(StateTransitionDictionary['drink'])
print(ObservationFunctionDictionary['drink'])

print(StateTransitionDictionary)
print(ObservationFunctionDictionary)

'''
StateTransitionDictionary={}
for k in root.findall('StateTransitionFunction'):
    for m in k.findall('CondProb'):
       for n in m.findall('Parameter'):
            for o in n.findall('Entry'):
                key = o.find('Instance').text.split(' ')[0]
                for p in o.findall('ProbTable'):
                    StateTransitionList=[]
                    pom2=p.text.split('\n')
                    for x in pom2:
                        pom3=x.split(' ')
                        for y in pom3:
                            if y!='':
                                StateTransitionList.append(float(y))
                StateTransitionVector=np.array(StateTransitionList).reshape(7,7)
                StateTransitionDictionary[key] = StateTransitionVector
print(StateTransitionDictionary['end'])


ObservationFunctionDictionary={}
for k in root.findall('ObsFunction'):
    for m in k.findall('CondProb'):
       for n in m.findall('Parameter'):
            for o in n.findall('Entry'):
                key = o.find('Instance').text.split(' ')[0]
                for p in o.findall('ProbTable'):
                    ObservationFunctionList=[]
                    pom2=p.text.split('\n')
                    for x in pom2:
                        pom3=x.split(' ')
                        for y in pom3:
                            if y!='':
                                ObservationFunctionList.append(float(y))
                ObservationFunctionVector=np.array(ObservationFunctionList).reshape(7,2)
                ObservationFunctionDictionary[key] = ObservationFunctionVector
print(ObservationFunctionDictionary['end'])
'''

print("Bok")












































'''
for child in root:
    if child.tag == 'Description' or child.tag == 'Discount':
        print(child.tag, child.text)
    elif child.tag == "Variable":
        for state_var in child.findall('StateVar'):
            print(state_var.tag, state_var.attrib, state_var.text)
            value_enum = state_var.findall('ValueEnum')
            print(value_enum[0].text)
        # print(child.tag, child.list(child.tag))

for child in root:
    for c in child:
        for k in c.findall('Parameter'):
           for m in k.findall('Entry'):
               for n in m.findall('Instance'):
                   print (n.text)

for child in root:
    for l in child.findall('StateVar'):
        print l.attrib['vnamePrev']
        print l.attrib.keys()
'''
