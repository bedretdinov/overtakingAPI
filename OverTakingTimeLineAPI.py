import requests
import json 


class OverTakingTimeLineAPI:
    
    def __init__(self, apikey, target, date, predict_freq, predict_interval):
        
        self.apikey = apikey
        self.target = target
        self.date = date
        self.freq = predict_freq
        self.period = predict_interval
        self.data = pd.DataFrame()
        
        self.api_set = {
            'apikey':apikey,
            'target':target,
            'date':date,
            'freq':predict_freq,
            'period':predict_interval
        }
         
    def predict(self):
        r = requests.get(  'http://overtaking.ru/api/predict_timeline/', data = json.dumps(self.api_set) ) 
        self.predict = r.json()
        self.data = pd.DataFrame(self.predict).sort_values('date')
        self.data['date'] = pd.to_datetime(self.data['date'])
        return self.data
    
    def show(self):
        plt.figure(figsize=(15,6))
        plt.xticks(rotation=60)
        now = self.data[self.data.date<pd.to_datetime('today')] 
        plt.plot(self.data['date'].values,self.data['target'].values, c='r', label='predict')
        plt.plot(now['date'].values,now['target'].values, c='b', label='real')
        plt.legend()
        plt.show()
