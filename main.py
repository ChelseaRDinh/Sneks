import bottle
import os
import random
import math
import time

#Run server in terminal with docker using the command:
#docker run -it --rm -p 3000:3000 sendwithus/battlesnake-server

#In separate window, run snake app with the following command:
#cd battlesnake
#python app/main.py

#When adding snake URL to game:
#make sure format is http://<local ip of machine>:8080
#since snake is configured to default to port 8080

#Indexing on board starts at 0 for width and length


@bottle.route('/')
def static():
    return "The server is running, hello there."


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    #data is dictionary object
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')
    data['name'] = 'Dwight'
    data['taunt'] = 'MICHAEEEEEEEEEEEEEEEEL'

    head_url = '%s://%s/static/dwight.gif' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#F96E07',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url
    }

def findFood(snake):
	data = bottle.request.json
	snek = snake
	foodList = data.get('food')['data']
	minX=100
	minY=100
	min_len=100
	for object in foodList:
		x= object['x']
		y= object['y']

		headX = snek['head']['x']
		headY = snek['head']['y']
		length = abs(headY-y) + abs(headX-x)
		
		print ([x,y])
		print([headX,headY])
		print 'food is this many steps away'
		print length
		print ''
		if length < min_len:
			minX = x
			minY = y
			min_len = length

	return [minX, minY]

@bottle.post('/move')
def move():
    count = 1
    #data variable is a dictionary
    data = bottle.request.json
    me = data.get('you')
    headx = me['body']['data'][0]['x']
    heady = me['body']['data'][0]['y']
    head = (headx, heady)
    midx = me['body']['data'][1]['x']
    midy = me['body']['data'][1]['y']
    mid = (midx, midy)
    tailx = me['body']['data'][2]['x']
    taily = me['body']['data'][2]['y']
    tail = (tailx, taily)

    snek = {'head': {'x': headx, 'y': heady}, 'body': {'x': midx, 'y': midy}, 'tail': {'x': tailx, 'y': taily}}

    print("My snek's current coordinates:")
    print(snek)
    print("\n")

    #See snake stats for each move

    # TODO: Do things with data

    directions = ['up', 'down', 'left', 'right']

    if snek['head']['x'] == 0:
        directions.remove('left')
    if snek['head']['y'] == 0:
        directions.remove('up')
    if snek['head']['x'] == data.get('width'):
        directions.remove('right')
    if snek['head']['y'] == data.get('height'):
        directions.remove('down')

    #check around head to make sure snake does not run into itself
    #check right
    if snek['head']['x']+1 == snek['body']['x'] or snek['head']['x']+1 == snek['tail']['x']:
        directions.remove('right')
    #check left
    if snek['head']['x']-1 == snek['body']['x'] or snek['head']['x']-1 == snek['tail']['x']:
        directions.remove('left')

    #check up
    if snek['head']['y']+1 == snek['body']['y'] or snek['head']['y']+1 == snek['tail']['y']:
        directions.remove('up')

    if snek['head']['y']-1 == snek['body']['y'] or snek['head']['y']-1 == snek['tail']['y']:
        directions.remove('down')

    direction = random.choice(directions)
    directions = directions


    return {
        'move': direction,
        'taunt': 'MICHAEEEEEEEEEEEEEEEEL'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'), debug = True)
