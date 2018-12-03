#==============================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#    Written: December 2018
#
#    Script to automate re-linking  Revit and CAD Links into
#    newly upgraded models to the new 003 Multiplex folder 
#    structure
#
#==============================================================#
import os

projfilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\1.0 QQT'
sitefilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\2.0 Site'
areafilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\3.0 Details\Areas'

BVNProjfiles = {
'AR-MOD-XX-XX-001': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-001-RVT - Site.rvt'),
'AR-MOD-XX-XX-002': os.path.join(projfilesfolder,'AR-MOD-XX-XX-002-RVT - Structure.rvt'),
'AR-MOD-XX-XX-003': os.path.join(projfilesfolder,'AR-MOD-XX-XX-003-RVT - Crown Louvers.rvt'),
'AR-MOD-XX-XX-004': os.path.join(projfilesfolder,'AR-MOD-XX-XX-004-RVT - Facade Tower.rvt'),
'AR-MOD-XX-XX-005': os.path.join(projfilesfolder,'AR-MOD-XX-XX-005-RVT - Basement & Poium.rvt'),
'AR-MOD-XX-XX-006': os.path.join(projfilesfolder,'AR-MOD-XX-XX-006-RVT - Interior Tower.rvt'),
'AR-MOD-XX-XX-009': os.path.join(projfilesfolder,'AR-MOD-XX-XX-009-RVT - MEP Place Holders.rvt'),
'AR-MOD-XX-XX-010': os.path.join(projfilesfolder,'AR-MOD-XX-XX-010-RVT - Master Grid.rvt'),
'AR-MOD-XX-XX-015': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-015-RVT - Clearance Zones.rvt'),
'AR-MOD-XX-XX-020': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-020-RVT - DCP Massing.rvt'),
'AR-MOD-XX-XX-800': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-800-RVT - MPX Site.rvt'),
'AR-MOD-XX-XX-900': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-900-RVT - Enscape 3D.rvt'),
'AR-MOD-XX-XX-999': os.path.join(areafilesfolder,'AR-MOD-XX-XX-999-RVT - Area Analysis Model.rvt')
}

ACONEXProjFiles = {
#ASPECT
'LA-MOD_XX_XX_001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ASPECT',
#AXIS
'AXS-HY-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\AXIS',
#BG&E
'ST-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\001 - ST-MOD-XX-XX-001-RVT - PODIUM',
'ST-MOD-XX-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\002 - ST-MOD-XX-XX-002-RVT - TOWER',
'ST-MOD-XX-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\003 - ST-MOD-XX-XX-003-RVT - EXISTING',
'ST-MOD-XX-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\004 - ST-MOD-XX-XX-004-RVT - 33A ALFRED',
'ST-MOD-XX-XX-005': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\005 - ST-MOD-XX-XX-005-RVT - INFILL',
'ST-MOD-XX-XX-007': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\007 - ST-MOD-XX-XX-007-RVT - CROWN',
#ECJV
'ECJ-ME-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ECJV',
#MPX
'MPX-PM-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\MPX',
#PFPS
'PFS-FS-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FS-MOD-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FD-MOD-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FS-MOD-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
#STAR
'STA-EL-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\STAR',
#WEBB
'ASP3-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\WEBB'
}

otherProjLinks = {
'Site Context.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BVN\Site Context',
'33 Alfred Interface.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\BVN',
'SU-MOD-XX-XX-001 - AAM Survey.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\AAM',
'AvroKO - CAD Links.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\2.0 AMPC\AvroKO',
'WEBB Substations CAD.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\WEBB',
'SE-ST-MOD - Levels B05 - L02.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L02 - L06.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L07 - L14.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L15 - L20.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
}

#'': r'',

# Is this link a BVN Project Link
# Look in BVNProjFiles dict using the full filename (No revision required)
# if '-RVT - ' in LinkName:
#   pass


# Is this link an Aconex Shared Project Link
# Look in the ACONEXProjFiles dict and do a lookup for latest revision
# if '-RVT-' in LinkName
#   pass

# If not then look in the last dict using full filename as key
# No revision

def main():
  pass


if __name__ == '__main__': main()