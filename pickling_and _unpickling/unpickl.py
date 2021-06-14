# unpickling method
import pickle, pickling_and_unpickling as cl
with open('pickling_File.txt', 'rb') as f:
    while True:
        try:
            data = pickle.load(f)
            data.disp()
        except Exception:
            print('Done')
            break