import os
import signal
import json
from flask import Flask, request, render_template
from buzz import generator, fizzbuzz, api, graph

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route('/')
def generator_page():
    return render_template('basic.html', content=generator.generate_buzz())


@app.route('/fizzbuzz')
def fizzbuzz_page():
    fizzbuzz_data = ' '.join(map(str, fizzbuzz.generate(0, 15).values()))
    return render_template('basic.html', content=fizzbuzz_data)


@app.route('/gif/<query>', endpoint='gif')
@app.route('/image/<query>', endpoint='image')
def image_search_page(query):
    url = {
        'image': api.image_search(query),
        'gif': api.gif_search(query),
    }[request.endpoint]
    if url:
        return render_template('image.html', url=url, alt=query)
    return render_template('basic.html', content="Couldn't find anything!")


@app.route('/graph/data')
def graph_data_page():
    graph_data = graph.generate_graph()
    return json.dumps(graph_data)


@app.route('/graph')
def graph_page():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
