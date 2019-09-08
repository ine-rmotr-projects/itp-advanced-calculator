from adv_calculator import * 

def test_add():
	result = add(1, 2, 3, 4, 5)
	assert result == 15

	result = add(1.22, .0023, 2.1, .98001)
	assert result == 4.30231


def test_multiply():
	result = multiply(1, 2, 3, 4, 5)
	assert result == 120

	result = multiply(1.22, .0023, 2.1, .98001)
	assert result == 0.005774806926000001


def test_maximum():
	result = maximum(1, 2, 3, 4, 5)
	assert result == 5

	result = maximum(1.22, .0023, 2.1, .98001)
	assert result == 2.1


def test_minimum():
	result = minimum(1, 2, 3, 4, 5)
	assert result == 1 

	result = minimum(1.22, .0023, 2.1, .98001)
	assert result == 0.0023


def test_mean():
	result = mean(1, 2, 3, 4 ,5)
	assert result == 3

	result = mean(1.22, .0023, 2.1, .98001)
	assert result == 1.0755775


def test_variance():
	result = variance(1, 2, 3, 4, 5)
	assert result == 2

	result = variance(1.22, .0023, 2.1, .98001)
	assert result == 0.5578392640187501


def test_std():
	result = std(1, 2, 3, 4, 5)
	assert result == 1.4142135623730951

	result = std(1.22, .0023, 2.1, .98001)
	assert result == 0.746886379591133
