# Statement Frequency Coverage

This is the official implemenation of the paper entitled Statement Frequency Coverage. In the ```example``` folder there is a file named ```cove.py``` which tracks
each test case. The ```cove.py``` is based on the ```unittest``` library. To change the implemenation from the ```unittest``` library to other test frameworks such as
```pytest```, you need to change the ```run_tests``` function. For example, to track each test case of the pytest framework, you need to change the body of the ```run_tests``` function
to ```pytest.main()```. After running ```cove.py```, the `tmp` folder is created. Put the content of that folder in the ```tmp```
directory in the root path of the project. Then, by running the ```SFC``` notebook, you are capable of computing the Statement Frequency Coverage.
