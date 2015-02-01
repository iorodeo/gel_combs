from __future__ import print_function

def get_well_width(L, n, p):
    well_width = L/(n+p*(n-1))
    return well_width



gel_length = 60.0
number_wells = 8 
well2gap_percent = 0.75

number_gaps = number_wells - 1

well_width = get_well_width(gel_length, number_wells, well2gap_percent)
gap_width = well2gap_percent*well_width



print('well width: ', well_width) 
print('gap  width: ', gap_width)

print(number_wells*well_width + (number_wells -1)*gap_width)


