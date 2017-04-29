from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.
class TweetDetailView(DetailView):
 
	queryset = Tweet.objects.all()

	def get_object(self):
		pk = self.kwargs.get("pk")
		obj = get_object_or_404(Tweet, pk)
		return obj
		# return Tweet.objects.get(pk)

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context



# def tweet_detail_view(request, id=1):
# 	tweet = Tweet.objects.get(id=id) # Get from Database
# 	print(tweet)
# 	data = {
# 		"tweet": tweet
# 	}
# 	return render(request, "tweets/detail_view.html", data)


# def tweet_list_view(request, id=1):
# 	tweet_list = Tweet.objects.all()
# 	print(tweet_list)
# 	data = {
# 		"tweets": tweet_list
# 	}
# 	return render(request, "tweets/list_view.html", data)