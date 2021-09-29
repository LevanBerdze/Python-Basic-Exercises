import math

l = float(input("Enter largest side length: "))
m = float(input("Enter middle side length: "))
s = float(input("Enter smallest side length: "))

def large_angles(l,m,s):
    return (l**2/(-2*m*s))+(m**2/(2*m*s))+(s**2/(2*m*s))

def middle_angle(l,l_angle,m):
    return m*(math.sin(l_angle))/l

def small_angle (l,l_angle,s):
    return s*(math.sin(l_angle))/l


l_angle = math.acos(large_angles(l,m,s))
l_angle_deg = math.degrees(l_angle)

m_angle = math.degrees(math.asin(middle_angle(l,l_angle,m)))

s_angle = math.degrees(math.asin(small_angle(l,l_angle,s)))
   

print(f'The angles are: \n {l_angle_deg:.6f} \n {m_angle:.6f} \n {s_angle:.6f}' )

