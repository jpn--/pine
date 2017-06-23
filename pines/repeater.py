import pandas


class call_me():
	def __init__(self, func):
		self._func = func
	def __call__(self, *arg, **kwarg):
		return self._func(*arg, **kwarg)



def external_repeater(func, kwarg_filename, *args, **kwargs):
	"""
	Use an external CSV file to iterate over keyword args passed to a function.
	
	Parameters
	----------
	func : callable
		This function gets called once for each row of the CSV file
	kwarg_filename : str
		A csv file containing keywork args (simple data types as read by pandas)
	
	Other Parameters
	----------------
	args 
		Positional arguments always passed to `func`
	kwargs 
		Common keyword arguments always passed to `func`
		
	Returns
	-------
	list
		A list containing the return value of `func` for each row
		of the csv file.
	"""
	result = []
	df = pandas.read_csv(kwarg_filename)
	direct_kw = {}
	indirect_kw = {}
	for k,v in kwargs.items():
		if isinstance(v,call_me):
			indirect_kw[k] = v
		else:
			direct_kw[k] = v
	for row in df.iterrows():
		local_kwargs = row[1].to_dict()
		indirect_kwargs = {k:v() for k,v in indirect_kw.items()}
		result.append(func(*args, **direct_kw, **indirect_kwargs, **local_kwargs))
	return result



if __name__=='__main__':
	from pprint import pprint
	f = lambda *a, **k: str(a)+"|"+str(k)
	
	iter = 1
	
	def hh():
		global iter
		iter += 1
		return iter
	
	t = external_repeater(f,'test/random_csv.csv', 12,13,14,fat='FAT', hhat=call_me(hh))
	for i in t:
		pprint(i)