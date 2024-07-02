def solution(chicken):
    service_chicken = 0
    coupons = chicken
    
    while coupons >= 10:
        service_chicken += coupons // 10
        coupons = (coupons // 10) + (coupons % 10)
    
    return service_chicken