import webapp2

class MainPage():
    def get(self):
        self.response.write("Hello word!!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
