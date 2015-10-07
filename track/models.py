from django.db import models

class Observation(models.Model):
	date = models.DateField('Observation Date')
	tempFLow = models.FloatField('Low Temperature (F)') #F is for fahrenheit
	tempFHigh = models.FloatField('High Temperature') #F is for fahrenheit
	tempFMean = models.FloatField('Average Temperature',blank=True,null=True)
	pressure = models.FloatField('Sea Level Pressure (in)',blank=True,null=True) #sea level pressure (in)
	wind = models.FloatField('Wind Speed (MPH)',blank=True,null=True) # (MPH)
	wind_direction_choices = (
		('N','North'),
		('S','South'),
		('E','East'),
		('W','West'),
		('NW','Northwest'),
		('NE','Northeast'),
		('SW','Southwest'),
		('SE','Southeast'),
		)
	windDirection = models.CharField('Wind Direction',max_length=2,
		choices=wind_direction_choices,
		blank=True,null=True
		)
	windMax = models.FloatField('Max Wind Speed',blank=True,null=True)
	visibility = models.FloatField('Visibility (Miles)',blank=True,null=True) #(miles)
	Rain = 'R'
	Snow = 'S'

	precip_type_choices = (
		(Rain,'Rain'),
		(Snow,'Snow'),
		)
	precip = models.FloatField('Precipitation',blank=True,null=True) # (inches)

	precipType = models.CharField('Precipitation Type',max_length=2,
		choices=precip_type_choices,
		blank=True,null=True)

