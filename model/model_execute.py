import subprocess
from os import path

from config import HEC_HMS_HOME, HEC_HMS_SH, HEC_DSSVUE_HOME, HEC_DSSVUE_SH, HEC_EVENT_SCRIPT,\
    PRE_PROCESSING_SCRIPT,POST_PROCESSING_SCRIPT, RAIN_FALL_FILE_NAME, DISCHARGE_FILE_NAME, \
    HEC_INPUT_DSS, HEC_OUTPUT_DSS


def execute_pre_dssvue(model_name, run_date_time):
    python_script_fp = PRE_PROCESSING_SCRIPT
    rain_csv_fp = RAIN_FALL_FILE_NAME.replace('{MODEL_NAME}', model_name).format(run_date_time)
    input_dss_fp = HEC_INPUT_DSS
    return _execute_hec_dssvue(python_script_fp, rain_csv_fp, input_dss_fp)


def execute_post_dssvue(model_name, run_date_time):
    python_script_fp = POST_PROCESSING_SCRIPT
    discharge_csv_fp = DISCHARGE_FILE_NAME.replace('{MODEL_NAME}', model_name).format(run_date_time)
    output_dss_fp = HEC_OUTPUT_DSS
    return _execute_hec_dssvue(python_script_fp, discharge_csv_fp, output_dss_fp)


def _execute_hec_dssvue(python_script_fp, csv_fp, dss_fp):
    dssvue_sh = path.join(HEC_DSSVUE_HOME, HEC_DSSVUE_SH)
    bash_command = '{dssvue_sh} {python_script} --csvfp {csv_fp} --dssfp {dss_fp}' \
        .format(dssvue_sh=dssvue_sh, python_script=python_script_fp, csv_fp=csv_fp, dss_fp=dss_fp)
    print('execute_hec_dssvue|bash_command : ', bash_command)
    ret_code = subprocess.call(bash_command, shell=True)
    return ret_code


def execute_hechms(model_name, run_path):
    hec_hms_sh_fp = path.join(HEC_HMS_HOME, HEC_HMS_SH)
    model_event_script_fp = path.join(run_path, HEC_EVENT_SCRIPT.replace('{MODEL_NAME}', model_name))
    bash_command = "{hec_hms_sh} -s {hec_event_script}" \
        .format(hec_hms_sh=hec_hms_sh_fp, hec_event_script=model_event_script_fp)
    print('execute_hechms|bash_command : ', bash_command)
    ret_code = subprocess.call(bash_command, shell=True)
    return ret_code
