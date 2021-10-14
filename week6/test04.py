def get_formatted_name(first, last):
    return f"{first}{last}".title()

def build_person(first,last,age=None):
    person = {'f':first, 'l':last}
    if age:
        person['a']=age
    return person

musician_list = []
musician_list.append(build_person('jimi','hendrix')) #{'f':'jimi', 'l':'hendrix'}
musician_list.append(build_person('sukjin','kim',age=27)) #{'f':'sukjin', 'l':'kim' , 'a'=27}

for m in musician_list:
    print(get_formatted_name(m['f'],m['l']))


