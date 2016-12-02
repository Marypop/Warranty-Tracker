# Warranty Tracker Web Application
A web application based on Flask, Python and MongoDB to help individuals track the warranties for their devices without hassle of maintaining various device documents.

To run or develop further, you will have to fulfill following dependencies,
- Python 3.x (3.5 used while developing this application)
- Mongo 3.0.6
- Flask
- dateutil (pip(x.x) install python-dateutil) [This is an additional module used for processing dates]
  { In case you multiple versions of python installed on the machine you may have to prefix `version` in place `x.x` }
- Flask-table (pip(x.x) install Flask-table) { version == 0.29 }
- Pymongo (pip(x.x) install pymongo)
 { To work with MongoDB, latest version would be preferred more details on http://api.mongodb.org/python/current/}
 
Currently, Application is configured to work on `host=localhost port=5555`.
For MongoDB, `db: 'test'` `Collection: userdb, deviceCollection, session` mongo service running with vanilla configuration.
 
At present, application does not show any errors or flash messages on bad user input or some other unexpected workflows, which is one of the areas for improvement, as well as a functionality to delete to the devices from the user profile and pagination.

