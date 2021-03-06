#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


from hookutils import collect_data_files


# On Linux pytz installed from distribution repository uses zoneinfo
# fron /usr/share/zoneinfo/ and no data files might be collected.
datas = collect_data_files('pytz')
