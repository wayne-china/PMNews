from tornado.web import RequestHandler

class MainHandler(RequestHandler):
	def get(self,template_variables = {}):
        news_timeline = self.news_model.get_all_news()
        template_variables["news_name"] = news_timeline["news_name"] 
        template_variables["news_link"] = news_timeline["news_link"]
        self.render("index.html",**template_variables)


# class SubscribeHandler(RequestHandler):
# 	def post(self):
# 		self.render("")

