### Old Code
def resolve_dependencies(dependencies):
    order = []
    for i in dependencies:
        print 'processing %s' % i
        if i in order:
            print '%s is in order' % i
            index = order.index(i)
            if dependencies[i]:
                for j in dependencies[i]:
                    order.insert(index,j)
            else:
                order.insert(0,i)
        else:        
            if dependencies[i]:
                for j in dependencies[i]:
                    order.append(j)
            order.append(i)        
        print order
    print order

### NewCode
class Service:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, service):
        self.dependencies.append(service)

    def __repr__(self):
        return '{ ' + ', '.join(self.dependencies) + ' }'


def initialize_service(service):
    serviceObj = Service(service)
    services[service] = serviceObj

def build_dependency(service, dependency):
    if service not in services:
        initialize_service(service)
        
    for i in dependency:
        if i not in services:
            initialize_service(i)
        services[service].add_dependency(i)

def resolve(resolver):
   for i in resolver:
       if i not in resolved_dependencies:
           for dependency in services[i].dependencies:  
                try:
                    resolve(dependency)
                except Exception:
                    print "Circular dependency"
           resolved_dependencies.append(i)
           
def resolve_and_print(dependencies):
    for service,dependency in dependencies.iteritems():
        build_dependency(service, dependency)
    print services    
    resolve(services)
    print resolved_dependencies
    print ''


dependencies = { '1' : [ '2', '5'], '2' : ['5' , '3'], '3' : [], '4': ['2', '3'], '5': ['3']}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
dependencies = { '1': ['9'], '4': ['5'], '9': [ '4' ]}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
dependencies = { '1': ['2'], '4': ['5']}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
dependencies = { '1': ['2'], '2' : ['3']}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
dependencies = { '1' : [ '2', '5'], '2' : ['5' , '3']}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
dependencies = { '1' : [ '2', '5'], '2' : ['5' , '3'], '3' : [], '5': ['8'], '4':     ['5'], '9': [ '4' ]}
services = {}
resolved_dependencies = []
resolve_and_print(dependencies)
