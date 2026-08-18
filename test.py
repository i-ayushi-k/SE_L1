from x import reg

def test_linear_regression():
    prediction = reg.predict([[5.0]])
    assert prediction[0] == 10.0
