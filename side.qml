// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick

ListView {
    
    required model

    delegate: Rectangle {
        // color: model.modelData.color
        required property string modelData
        height: 25
        width: 100
        Text { text: parent.modelData }
    }
}