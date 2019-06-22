import sys
import numpy as np


def ip(r, w, sou, c):
    """
    Returns one array
    [z, ip]
    ip: calculates the incident pressure (ip) in kPa or psi
    at a distance (r) in meters or feet from charge type:
    spherical-free-air-burst (sfab) or hemispherical-surface-burst (hsb).
    The system of units are meters, kilogram, seconds (mks) or
    ft, pound, second (fps).  The charge mass must be in TNT
    equivalent kg or lb.  The calculated scaled distance will be
    in m/(kg)^1/3 or ft/(lb)^1/3.
    S. Kevin McNeill, 1.0 (Explicitly not copyrighted).
    This function is released to the public domain; Any use is allowed.

    Example:
    import kingery_bulmash as kb
    distance = 50 #m
    charge weight = 1 #kg
    units = mks
    charge = sab
    params = kb.ip(distance, weight, units, charge)
    """
    zlog = np.log10(r)
    if c == "sfab":
        # Free-Air Burst
        if sou == "fps":
            # feet pound seconds
            # valid r (0.134 - 100.0ft)
            u = [-0.756579301809, 1.35034249993]
            y = [1.77284970457, -1.69012801396,
                0.00804973591951, 0.336743114941,
                -0.00516226351334, -0.0809228619888,
                -0.00478507266747, 0.00793030472242,
                0.0007684469735]

            u_ip = u[0] + u[1] * zlog
            ip = 10**(y[0] + y[1] * u_ip +
                      y[2] * u**2 + y[3] * u_ip**3 +
                      y[4] * u**4 + y[5] * u_ip**5 +
                      y[6] * u**6 + y[7] * u_ip**7 +
                      y[8] * u_ip**8)
            z = r / w**(1 / 3)
            return z, ip
        elif sou == "mks":
            # meters kilogram seconds
            # valid r (0.0531 - 40.0m)
            u = [-0.214362789151, 1.35034249993]
            y = [2.611368669, -1.69012801396,
                 0.00804973591951, 0.336743114941,
                 -0.00516226351334, -0.0809228619888,
                 -0.00478507266747, 0.00793030472242,
                 0.0007684469735]
            u_ip = u[0] + u[1] * zlog
            ip = 10**(y[0] + y[1] * u_ip +
                     y[2] * u_ip**2 + y[3] * u_ip**3 +
                     y[4] * u_ip**4 + y[5] * u_ip**5 +
                     y[6] * u_ip**6 + y[7] * u_ip**7 +
                     y[8] * u_ip**8)
            z = r / w**(1 / 3)
            return z, ip
        else:
            print("Units input: {}, must be mks or fps".format(sou))
    elif c == "hsb":
        # Hemispherical Surface Burst
        if sou == "fps":
            # feet pound seconds
            # valid r (0.134 - 100.0ft)
            u = [-0.756579301809, 1.35034249993]
            y = [1.9422502013, -1.6958988741,
                -0.154159376846, 0.514060730593,
                0.0988534365274, -0.293912623038,
                -0.0268112345019, 0.109097496421,
                0.00162846756311, -0.0214631030242,
                0.0001456723382, 0.00167847752266]

            u_ip = u[0] + u[1] * zlog
            ip = 10**(y[0] + y[1] * u_ip +
                      y[2] * u_ip**2 + y[3] * u_ip**3
                      + y[4] * u_ip**4 + y[5] * u_ip**5
                      + y[6] * u_ip**6 + y[7] * u_ip**7
                      + y[8] * u_ip**8 + y[9] * u_ip**9
                      + y[10] * u_ip**10 + y[11] * u_ip**11)
            z = r / w**(1 / 3)
            return z, ip
        elif sou == "mks":
           # meters kilogram seconds
           # valid r (0.0531 - 40.0m)
           u=[-0.214362789151, 1.35034249993]
           y=[2.78076916577, -1.6958988741,
                -0.154159376846, 0.514060730593,
                0.0988534365274, -0.293912623038,
                -0.0268112345019, 0.109097496421,
                0.00162846756311, -0.0214631030242,
                0.0001456723382, 0.00167847752266]
           u_ip=u[0] + u[1] * zlog
           ip=10**(y[0] + y[1] * u_ip +
                     y[2] * u_ip**2 + y[3] * u_ip**3 +
                     y[4] * u_ip**4 + y[5] * u_ip**5 +
                     y[6] * u_ip**6 + y[7] * u_ip**7 +
                     y[8] * u_ip**8 + y[9] * u_ip**9 +
                     y[10] * u_ip**10 + y[11] * u_ip**11)
           z = r / w**(1 / 3)
           return z, ip
        else:
            print("Units input: {}, must be mks or fps".format(sou))
    else:
        print("Charge type input: {} must be sfab or hsb".format(c))

def ii1(r, w, sou, c):
    """
    Returns one array
    [z, ii]
    ii1: (r = 0.134 - 2.00ft) calculates the incident impulse (ip) in kPa-ms
    or psi-ms at a distance (r) in meters or feet from charge type:
    spherical-free-air-burst (sfab) or hemispherical-surface-burst (hsb).
    The system of units are meters, kilogram, seconds (mks) or
    ft, pound, second (fps).  The charge mass must be in TNT
    equivalent kg or lb.  The calculated scaled distance will be
    in m/(kg)^1/3 or ft/(lb)^1/3.
    S. Kevin McNeill, 1.0 (Explicitly not copyrighted).
    This function is released to the public domain; Any use is allowed.

    Example:
    import kingery_bulmash as kb
    distance = 50 #m
    charge weight = 1 #kg
    units = mks
    charge = sab
    params = kb.ii(distance, weight, units, charge)
    """
    zlog = np.log10(r)
    if c == "sfab":
        # Free-Air Burst
        if sou == "fps":
            # feet pound seconds
            # valid r (0.134 - 2.00ft)
            u = [1.04504877747, 3.24299066475]
            y = [1.43534136453, -0.443749377691,
                0.168825414684, 0.0348138030308,
                -0.010435192824]

            u_ii1 = u[0] + u[1] * zlog
            ii1 = 10**(y[0] + y[1] * u_ip +
                      y[2] * u**2 + y[3] * u_ip**3 +
                      y[4] * u**4)
            z = r / w**(1 / 3)
            return z, ip
        elif sou == "mks":
            # meters kilogram seconds
            # valid r (0.0531 - 0.792m)
            u = [2.34723921354, 3.24299066475]
            y = [1.43534136453, -0.443749377691,
                0.168825414684, 0.0348138030308,
                -0.010435192824]

            u_ii1 = u[0] + u[1] * zlog
            ii1 = 10**(y[0] + y[1] * u_ip +
                      y[2] * u**2 + y[3] * u_ip**3 +
                      y[4] * u**4)
            u_ip = u[0] + u[1] * zlog
            ip = 10**(y[0] + y[1] * u_ip +
                     y[2] * u_ip**2 + y[3] * u_ip**3 +
                     y[4] * u_ip**4 + y[5] * u_ip**5 +
                     y[6] * u_ip**6 + y[7] * u_ip**7 +
                     y[8] * u_ip**8)
            z = r / w**(1 / 3)
            return z, ip
        else:
            print("Units input: {}, must be mks or fps".format(sou))
    elif c == "hsb":
        # Hemispherical Surface Burst
        if sou == "fps":
            # feet pound seconds
            # valid r (0.134 - 100.0ft)
            u = [-0.756579301809, 1.35034249993]
            y = [1.9422502013, -1.6958988741,
                -0.154159376846, 0.514060730593,
                0.0988534365274, -0.293912623038,
                -0.0268112345019, 0.109097496421,
                0.00162846756311, -0.0214631030242,
                0.0001456723382, 0.00167847752266]

            u_ip = u[0] + u[1] * zlog
            ip = 10**(y[0] + y[1] * u_ip +
                      y[2] * u_ip**2 + y[3] * u_ip**3
                      + y[4] * u_ip**4 + y[5] * u_ip**5
                      + y[6] * u_ip**6 + y[7] * u_ip**7
                      + y[8] * u_ip**8 + y[9] * u_ip**9
                      + y[10] * u_ip**10 + y[11] * u_ip**11)
            z = r / w**(1 / 3)
            return z, ip
        elif sou == "mks":
           # meters kilogram seconds
           # valid r (0.0531 - 40.0m)
           u=[-0.214362789151, 1.35034249993]
           y=[2.78076916577, -1.6958988741,
                -0.154159376846, 0.514060730593,
                0.0988534365274, -0.293912623038,
                -0.0268112345019, 0.109097496421,
                0.00162846756311, -0.0214631030242,
                0.0001456723382, 0.00167847752266]
           u_ip=u[0] + u[1] * zlog
           ip=10**(y[0] + y[1] * u_ip +
                     y[2] * u_ip**2 + y[3] * u_ip**3 +
                     y[4] * u_ip**4 + y[5] * u_ip**5 +
                     y[6] * u_ip**6 + y[7] * u_ip**7 +
                     y[8] * u_ip**8 + y[9] * u_ip**9 +
                     y[10] * u_ip**10 + y[11] * u_ip**11)
           z = r / w**(1 / 3)
           return z, ip
        else:
            print("Units input: {}, must be mks or fps".format(sou))
    else:
        print("Charge type input: {} must be sfab or hsb".format(c))
