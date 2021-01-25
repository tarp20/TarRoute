from trains.models import Train



def dfs_paths(praph,start,goal):
    stack = [(start,[start])]
    while stack:
        (vertex,path) = stack.pop()
        if vertex in praph.keys():
            for next_ in praph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_,path+[next_]))




def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.city_from_id,set())
        graph[q.city_from_id].add(q.city_to_id)
    return graph





def get_routes(request,form) -> dict:
    context = {'form':form}
    qs = Train.objects.all().select_related('city_from','city_to')
    graph = get_graph(qs)
    data = form.cleaned_data
    city_from = data['city_from']
    city_to = data['city_to']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph,city_from.id,city_to.id))
    if not len(all_ways):
        raise ValueError('There is no route for this request')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Route through these cities is not possible')
    else:
        right_ways = all_ways
    routes = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.city_from_id, q.city_to_id),[])
        all_trains[(q.city_from_id,q.city_to_id)].append(q)
        for route in right_ways:
            tmp = {}
            tmp['trains'] = []
            total_time = 0
            for i in range(len(route)-1):
                qs = all_trains[(route[i], route[i+1] )]
                q = qs[0]
                total_time +=q.travel_time
                tmp['trains'].append(q)
            tmp['total_time'] = total_time
            if total_time <= travelling_time:
                routes.append(tmp)
    if not routes:
        raise ValueError('Travel time is longer than specified')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes ))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'city_from':city_from,'city_to':city_to}
    return context








