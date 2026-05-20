/*!
 * \file prelu_tiling_key.h
 * \brief Tiling 模板参数定义
 */

#ifndef __PRELU_TILING_KEY_H__
#define __PRELU_TILING_KEY_H__

#include "ascendc/host_api/tiling/template_argument.h"

#define PRELU_TPL_SCH_MODE_0 0
#define PRELU_TPL_SCH_MODE_1 1

ASCENDC_TPL_ARGS_DECL(
    Prelu,
    ASCENDC_TPL_UINT_DECL(
        schMode, 1, ASCENDC_TPL_UI_LIST, PRELU_TPL_SCH_MODE_0, PRELU_TPL_SCH_MODE_1));

ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(
    ASCENDC_TPL_UINT_SEL(schMode, ASCENDC_TPL_UI_LIST, PRELU_TPL_SCH_MODE_0, PRELU_TPL_SCH_MODE_1)));

#endif
