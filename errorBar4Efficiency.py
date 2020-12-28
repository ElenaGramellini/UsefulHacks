def calculateErrorBar (num, den):
    if den:
        return TMath.Sqrt(num/(den*den)*(1-num/den)   )
    else:
        return 0
