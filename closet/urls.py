from django.conf.urls import include, url,static
urlpatterns=[
	url(r'^update/$','closet.views.update',name='update'),
	url(r'^top/$','closet.views.giveTop',name='giveTop'),
	url(r'^bottom/$','closet.views.giveBottom',name='giveBottom'),
	url(r'^foot/$','closet.views.giveFoot',name='giveFoot'),
	url(r'^acc/$','closet.views.giveAcc',name='addAcc'),
	url(r'^addFav/$','closet.views.addCombination',name='addFav'),
	url(r'^getFav/$','closet.views.getCombination',name='getFav'),
	url(r'^wearToday/$','closet.views.wearToday',name='wearToday'),
	url(r'^getFriendFav/$','closet.views.getFriendCombination',name='getFriendFav'),
	#url(r'^getFriendToday/$','closet.views.getFriendTodayCombination',name='getFriendToday'),
]