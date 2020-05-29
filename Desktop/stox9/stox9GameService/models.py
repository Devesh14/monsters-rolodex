from django.db import models


class userPortfolio(models.Model):
    portfolioId = models.CharField(max_length=100, blank=True)
    eventId = models.CharField(max_length=100, blank=True)
    portfolioName = models.CharField(max_length=100, blank=True, default = '')
    portfolioIndex = models.CharField(max_length=100, blank=True, default = '')
    userId = models.CharField(max_length=100, blank=True, default = '')
    userUniqueId = models.CharField(max_length=100, blank=True, default = '')
    status =  models.IntegerField(blank=True, null=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)
    cloned_from = models.CharField(max_length=100, blank=True, default = '')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.portfolioId

class contestPortfolio(models.Model):
    contestId = models.CharField(max_length=100, blank=True, default='')
    eventId = models.CharField(max_length=100, blank=True)
    portfolioId = models.CharField(max_length=100, blank=True)
    planId = models.CharField(max_length=100, blank=True, default = '')
    poolId = models.CharField(max_length=100, blank=True, default = '')
    userId = models.CharField(max_length=100, blank=True, default = '')
    userUniqueId = models.CharField(max_length=100, blank=True, default = '')
    totalPoints =  models.IntegerField(blank=True, null=True)
    wonTurtles =  models.IntegerField(blank=True, null=True)
    rank =  models.IntegerField(blank=True, null=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)
    refTxnId = models.CharField(max_length=100, blank=True, default = '')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.contestId

class plan(models.Model):
    planId = models.CharField(max_length=100, blank=True, default = '')
    isConfirmWinnings = models.BooleanField(blank=True, default=False)
    isDefault = models.BooleanField(blank=True, default=False)
    isRepetitive = models.BooleanField(blank=True, default=False)
    isActive = models.BooleanField(blank=True, default=False)
    maxTeams =  models.IntegerField(blank=True, null=True)
    canApplyBonus = models.BooleanField(blank=True, default=False)
    canApplyPass = models.BooleanField(blank=True, default=False)
    entryFee =  models.IntegerField(blank=True, null=True)
    totalWinners =  models.IntegerField(blank=True, null=True)
    rake =  models.IntegerField(blank=True, null=True)
    prizePool =  models.IntegerField(blank=True, null=True)
    winDistributions = [ 
        ('startRank', 'endRank', 'totalUsers', 'prizeMoney', 'totalPrize')
    
    ]
    lastUpdated = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.planId

class pool(models.Model):
    contestId = models.CharField(max_length=100, blank=True, default='')
    eventId = models.CharField(max_length=100, blank=True)
    poolId = models.CharField(max_length=100, blank=True)
    planId = models.CharField(max_length=100, blank=True, default = '')
    isCancelled = models.BooleanField(blank=True, default=False)
    isFilled = models.BooleanField(blank=True, default=False)
    paymentStatus = models.BooleanField(blank=True, default=False)
    spotsLeft =  models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.poolId


