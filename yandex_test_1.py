import json

with open('input_1.txt') as json_file:
    input_data = json.load(json_file)

res = {}

for event in input_data:
    if event['order_id'] not in res.keys():
        res[event['order_id']] = [{
            'item_id': event['item_id'],
            'event_id': event['event_id'],
            'total_count': event['count'] - event['return_count'],
            'status': event['status']
        }]
    order_items_id = []
    for i in range(len(res[event['order_id']])):
        order_items_id.append(res[event['order_id']][i]['item_id'])
    if event['item_id'] not in order_items_id:
        res[event['order_id']].append({
            'item_id': event['item_id'],
            'event_id': event['event_id'],
            'total_count': event['count'] - event['return_count'],
            'status': event['status']
        })
    for item in res[event['order_id']]:
        if item['item_id'] == event['item_id'] and item['event_id'] < event['event_id']:
            item['total_count'] = event['count'] - event['return_count']
            item['status'] = event['status']

result = []
orders = []

for order in res.keys():
    for item in res[order]:
        if item['status'] == 'CANCEL' or item['total_count'] <= 0:
            continue
        if order not in orders:
            orders.append(order)
            result.append({
                'id': order,
                'items': [{
                    'count': item['total_count'],
                    'id': item['item_id']
                }]
            })
        else:
            index = orders.index(order)
            result[index]['items'].append({
                'count': item['total_count'],
                'id': item['item_id']
            })
result = sorted(result, key=lambda k: k['id'], reverse=False)

with open('output_1.txt', 'w') as outfile:
    json.dump(result, outfile, indent=4, sort_keys=True)     