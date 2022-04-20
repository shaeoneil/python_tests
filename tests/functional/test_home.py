def test_index_route(app,client):
    """
    GIVEN a flask application is configured for testing 
    WHEN the '/' route is requested (GET)
    THEN chdck that the response is valid
    """
    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Verticle Tank Maintenance" in res.data 
        assert b"VTM Page Welcome!" in res.data
    



def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    print("-- /about GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"Verticle Tank Maintenance" in res.data
        assert b"About Verticle Tank Maintenance" in res.data


def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the correct page is displayed
    """
    print("-- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Estimate" in res.data
        assert b"Recieve Estimate:" in res.data

def test_estimate_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'calculate' button is selected (POST)
    THEN check that the correct estimate is returned to the user
    """
    print("-- /estimate 'estimate' POST test")
    # Functional test - it puts POST data in the age route and looks for the correct value to be returned
    # individual functions to perform the calculations are tested in the Unit tests
    with app.test_client() as test_client:
        # pass in the data use Chrome Developer Tools -> Network -> Click on page -> Payload
        # passing future age value as 'x' because I look for the key(future_age), not the value in app.py if/then stmt
        calc_estimate = {"radius":"180", "height":"360", "estimate":"x"} 
        res = test_client.post('/estimate', data=calc_estimate)
        assert res.status_code == 200 
        assert b"$141,300.00" in res.data 