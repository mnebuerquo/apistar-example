# Apistar sample app

How to run:

1. `docker-compose up`
2. `curl http://localhost:5000` - to see welcome message
3. Open [http://localhost:8081/](http://localhost:8081/) in your browser.
4. Open [http://localhost:8081/swagger](http://localhost:8081/swagger) in your browser.
5. `wget -qO- "http://localhost:5000/schema" > schema.json`
6. Open [http://editor.swagger.io](http://editor.swagger.io) in your browser and
   upload your `schema.json` which you created in the previous step.

# Errors

```
Schema error at paths['/'].get
should have required property 'responses'
missingProperty: responses

Schema error at paths['/new'].post
should have required property 'responses'
missingProperty: responses

Schema error at paths['/list'].get
should have required property 'responses'
missingProperty: responses

Schema error at paths['/game/{gameid}'].get
should have required property 'responses'
missingProperty: responses

Schema error at paths['/game/{gameid}/move'].post
should have required property 'responses'
missingProperty: responses

Schema error at paths['/game/{gameid}/wait'].get
should have required property 'responses'
missingProperty: responses
```
