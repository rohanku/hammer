import importlib
from hammer.vlsi import CLIDriver, HammerTool, HammerToolHookAction

# to be inserted post- route_design
def hack_iquantus(x: HammerTool) -> bool:

    # TODO elam fix hardcode
    # Only add qrc file post route so we can use iquantus (and our custom qrc lef map, else tquantus will generate its own incorrect map)
    x.append(f'''
create_rc_corner -name ff_n40C_1v95.hold_rc -temperature -40.0 -qrc_tech /home/ff/eecs251b/sp24-workspace/hacked_techfile_from_cadence/qrcTechFile
create_rc_corner -name tt_025C_1v80.extra_rc -temperature 25.0 -qrc_tech /home/ff/eecs251b/sp24-workspace/hacked_techfile_from_cadence/qrcTechFile
create_rc_corner -name ss_100C_1v60.setup_rc -temperature 100.0 -qrc_tech /home/ff/eecs251b/sp24-workspace/hacked_techfile_from_cadence/qrcTechFile
set_db extract_rc_effort_level high
set_db extract_rc_lef_tech_file_map {importlib.resources.files("hammer.technology.sky130").joinpath("qrc_lef.map")}
set_db extract_rc_engine post_route
    ''')
    return True
