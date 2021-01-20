from json import dumps
result = [{}, {}]
with open('7.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        name, type_of_firm, profit, costs = line.split()
        result[0][name] = int(profit) - int(costs)
    result[1]['average_profit'] = round(sum(
        profit for type_of_firm, profit in result[0].items() if profit > 0) / len(result[0]))
    with open('7.json', "w", encoding='utf-8') as dst:
        dst.write(dumps(result))
