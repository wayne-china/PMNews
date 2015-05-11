from tornado.web import RequestHandler

class MainHandler(RequestHandler):
	def get(self,template_variables = {}):
        news_timeline = self.news_model.get_all_news()
        template_variables["news_name"] = news_timeline["news_name"] 
        template_variables["news_link"] = news_timeline["news_link"]
        self.render("index.html",**template_variables)


class AdminHandler(RequestHandler):
	@tornado.web.authenticated
	def get(self,template_variables = {}):
		news_timeline = self.news_model.get_all_news()
		self.render("admin.html")


class AddHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self,template_variables = {}):
		self.render("add.html")

	@tornado.web.authenticated
	def post(self,template_variables = {}):
		news_name = self.get_argument("news")
		news_link = self.get_argument("link")
		try:
			self.news_model.add_news(news_name,news_link)
			return self.write("success")
		except Exception,e:
			print (e)

class Detailhandler(BaseHandler):
	@tornado.web.authenticated
	def get(self,template_variables = {}):
		if(re.match(r'^\d+$', uid)):
            news = self.user_model.get_news_by_uid(uid)
        else:
		    return self.write("news not found")
		template_variables["news"] = news
		self.render("detail.html",**template_variables)


# class SubscribeHandler(RequestHandler):
# 	def post(self):
# 		self.render("")

