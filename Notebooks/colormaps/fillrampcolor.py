#! /usr/bin/env hython

import hou
import types

## Thanks!! to: http://forums.odforce.net/topic/20327-programmatically-modifying-a-color-ramp/
# for explaining how to do this.  The documentation I could find gave no clue.
# Edited by AJ to use for color ramps instead of spline ramps

def mapfunc(lineno, linetext):
    nlines = 1000
    vfrom, vto = 0.0, 1.0
    return lineno * (vto-vfrom) / nlines + vfrom


def fillramp(voppath, rampname, filename, column=2, keycolumn=1):
    """fillramp(voppath, rampname, filename, column):
	AJ update
	Load keys/values for a Houdini ramp with values from a file.
	voppath -- path string, e.g. '/obj/solar_core/update_density_volume_VOP'
	rampname -- which ramp in that VOP to update
	filename -- name of text file with space-separated fields.  First line is skipped.  
	column -- values come from that column (leftmost is column 1).
	keycolumn -- ramp keys come from that column (keycolumn=1 by default).
	    If keycolumn=None, the key is the line number (0-based).
	    If keycolumn is a floating-point number, the key is the line number times that multiplier.
	    If keycolumn is a function, it's called with two args: the line number and text of the line
    e.g.
    # fill ramp with mapping from column_1 value to column_2 value
    fillramp.fillramp("/obj/name_of_VOP", "ramp_in_that_VOP", "textfile.dat", column=2)
    # fill ramp with mapping from rescaled line number (line 0 -> 0.0, line 1000 -> 10.0) to column_1 value
    fillramp.fillramp("/obj/name_of_VOP", "name_of_ramp", "textfile.dat", column=1, keycolumn=lambda lineno, line: lineno*10.0/1000 + 0)
    """

    vopnode = hou.node(voppath)
    if vopnode is None:
	raise ValueError("fillramp: no node named %s" % voppath)
    parm = vopnode.parm(rampname)
    if parm is None:
	raise ValueError("fillramp: node %s doesn't contain a ramp named %s" % (voppath, rampname))

    with open(filename) as f:
	f.next()  ; # skip first (header) line
	keys = []
	vals = []
	lineno = 0
	for line in f:
	    ss = line.split()
	    if len(ss) >= column:
		if isinstance(keycolumn, int):
		    key = float(ss[keycolumn-1])
		elif isinstance(keycolumn, float):
		    key = lineno * keycolumn
		elif isinstance(keycolumn, types.LambdaType):
		    key = keycolumn(lineno, line)
		else:
		    key = lineno
		keys.append( key )
		vals.append( (float(ss[column-1]),float(ss[column]),float(ss[column+1])) )
		lineno += 1

    parm.set( len(keys) )
    for k in range(len(keys)):
	what = "%s%dpos" % (rampname, k+1)
	kparm = vopnode.parm(what)  # "pos" for this key
	if kparm is None:
	    raise ValueError("fillramp: %s ramp %s has no position-param %s?" % (voppath, rampname, what))
	kparm.set( keys[k] )

	what = "%s%dcr" % (rampname, k+1)
	vparm = vopnode.parm(what)  # "red" for this key
	if vparm is None:
	    raise ValueError("fillramp: %s ramp %s has no value-param %s?" % (voppath, rampname, what))
	vparm.set( vals[k][0] )

	what = "%s%dcg" % (rampname, k+1)
	vparm = vopnode.parm(what)  # "green" for this key
	if vparm is None:
	    raise ValueError("fillramp: %s ramp %s has no value-param %s?" % (voppath, rampname, what))
	vparm.set( vals[k][1] )

	what = "%s%dcb" % (rampname, k+1)
	vparm = vopnode.parm(what)  # "blue" for this key
	if vparm is None:
	    raise ValueError("fillramp: %s ramp %s has no value-param %s?" % (voppath, rampname, what))
	vparm.set( vals[k][2] )

	what = "%s%dinterp" % (rampname, k+1)
	iparm = vopnode.parm(what)
	if iparm is None:
	    raise ValueError("fillramp: %s ramp %s has no interpolation-param %s?" % (voppath, rampname, what))
	iparm.set( 1 ) # linear interpolation (?)

print fillramp.__doc__
