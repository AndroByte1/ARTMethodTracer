from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import threading
import os
import tempfile
import time
from PyQt5.QtCore import QStringListModel 
import frida


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a vertical layout for the main window
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Create horizontal layouts for each section
        # Device section
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_1.addWidget(self.label)
        
        self.device_list = QtWidgets.QComboBox(self.centralwidget)
        self.device_list.setObjectName("device_list")
        self.device_list.addItem("")
        self.horizontalLayout_1.addWidget(self.device_list)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load_devices)
        self.horizontalLayout_1.addWidget(self.pushButton_2)
        
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        
        # Apps section
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        
        self.Applist = QtWidgets.QComboBox(self.centralwidget)
        self.Applist.setObjectName("Applist")
        self.Applist.addItem("")
        self.horizontalLayout_2.addWidget(self.Applist)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_apps)
        self.horizontalLayout_2.addWidget(self.pushButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        # Classes section
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.list_classes_exact)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        
        '''
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        # REMOVED: self.pushButton_4.clicked.connect(self.monitor_all_methods)
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.listView.setObjectName("listView")
        ''' 
        # to add click event on method text
        #self.listView.clicked.connect(self.on_method_clicked)



        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        # Status label
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        
        # Create a horizontal layout for the main content area
        self.horizontalLayout_main = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        
        # Left side - Methods section
        self.verticalLayout_left = QtWidgets.QVBoxLayout()
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_left.addWidget(self.label_4)
        
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_left.addWidget(self.listView)
        self.listView.clicked.connect(self.on_method_clicked)
        
        self.horizontalLayout_main.addLayout(self.verticalLayout_left)
        
        # Right side - Consoles
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setObjectName("verticalLayout_right")
        
        # Upper console
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_right.addWidget(self.label_5)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_right.addWidget(self.plainTextEdit)
        
        # Lower console
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_right.addWidget(self.label_6)
        
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_right.addWidget(self.plainTextEdit_2)
        
        # Run code button
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_right.addWidget(self.pushButton_5)
        
        self.horizontalLayout_main.addLayout(self.verticalLayout_right)
        
        # Add the main content layout
        self.verticalLayout.addLayout(self.horizontalLayout_main)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Variables for frida process
        self.frida_process = None
        self.is_monitoring = False
        self.classes_set = set()  # Store unique classes
        self.package_name = ""
        
        # Store reference to MainWindow for signals
        self.main_window = MainWindow
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Load devices when app starts
        self.init_method_tree()
        self.load_devices()
        
        # Connect comboBox signal to show methods when class is selected
        self.comboBox.currentTextChanged.connect(self.show_class_methods)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frida Tool"))
        self.label.setText(_translate("MainWindow", "Device:"))
        self.device_list.setItemText(0, _translate("MainWindow", "Select device"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))
        self.label_2.setText(_translate("MainWindow", "Apps:"))
        self.Applist.setItemText(0, _translate("MainWindow", "Click Connect"))
        self.pushButton.setText(_translate("MainWindow", "Apps"))
        self.label_3.setText(_translate("MainWindow", "Classes:"))
        self.pushButton_3.setText(_translate("MainWindow", "List Classes"))
      #  self.pushButton_4.setText(_translate("MainWindow", "Monitor All"))
        self.label_4.setText(_translate("MainWindow", "Methods"))
        self.label_5.setText(_translate("MainWindow", "Method Trace Console"))
        self.label_6.setText(_translate("MainWindow", "Console"))
        self.pushButton_5.setText(_translate("MainWindow", "Run code"))
        self.status_label.setText(_translate("MainWindow", "Ready"))

    def load_devices(self):
        """Load USB devices when app starts"""
        try:
            self.device_list.clear()
            self.device_list.addItem("Select device")
            
            # Get devices from frida (using frida-python bindings)
            devices = frida.enumerate_devices()
            # Add USB devices
            for dev in devices:
                if dev.type == "usb":
                    self.device_list.addItem(f"{dev.name}")
            
            self.status_label.setText(f"Found {self.device_list.count()-1} USB device(s)")
        except Exception as e:
            self.status_label.setText(f"Error loading devices: {str(e)}")
            self.device_list.addItem("Error: Could not load devices")

    def load_apps(self):
        """Load apps from the device selected in dropdown"""
        try:
            self.Applist.clear()
            device_name = self.device_list.currentText()
            
            if device_name == "Select device" or not device_name:
                self.status_label.setText("Please select a device first")
                self.Applist.addItem("Select a device first")
                return
            
            # Get devices from frida (using frida-python bindings)
            devices = frida.enumerate_devices()
            for dev in devices:
                if dev.name == device_name and dev.type == "usb":
                    # Get apps from this device
                    apps = dev.enumerate_applications()
                    app_count = 0
                    for app in apps:
                        self.Applist.addItem(f"{app.name}")
                        app_count += 1
                    self.status_label.setText(f"Loaded {app_count} app(s) from {device_name}")
                    break
        except Exception as e:
            self.status_label.setText(f"Error loading apps: {str(e)}")
            self.Applist.addItem("Error loading apps")

    def show_class_methods(self):
        """Show methods for the selected class when user selects a class from dropdown"""
        try:
            selected_class = self.comboBox.currentText()
            if not selected_class or selected_class == "":
                return
                
            # Clear the method list and show only methods for this class
            self.methodModel.clear()
            self.methodModel.setHorizontalHeaderLabels([f"Methods for {selected_class}"])

            if self.Applist.currentIndex() < 0 or self.Applist.currentText() == "Click Connect":
                self.status_label.setText("Please select an app first")
                return
            
            app_name = self.Applist.currentText()
            device_name = self.device_list.currentText()

            if device_name == "Select device":
                self.status_label.setText("Please select a device first")
                return
            
            # Get PID using frida-python
            pid = self.get_pid_for_app(app_name, device_name)
            if not pid:
                self.status_label.setText(f"Could not find PID for {app_name}. Make sure app is running.") 
                return
            
            # Get package name
            package_name = self.get_package_for_app(app_name, device_name)
            if not package_name:
                self.status_label.setText(f"Could not get package name for {app_name}")
                return
            
            self.status_label.setText(f"Loading methods for class: {selected_class}")
            
            # Clear console
            self.plainTextEdit_2.clear()
            
            # Start a thread to get methods for this specific class
            thread = threading.Thread(
                target=self.get_class_methods, 
                args=(selected_class, pid), 
                daemon=True
            )
            thread.start()
            
        except Exception as e:
            self.status_label.setText(f"Error showing class methods: {str(e)}")
    
    def on_method_clicked(self, index):
        item = self.methodModel.itemFromIndex(index)
        if item:
            method_text = item.text()
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(f"Selected method: {method_text}")
            lines = method_text.split('\n')
            if len(lines) >= 2:
                class_name = lines[0].strip()
                method_sig = lines[1].strip()
            
            # Start tracing
            self.trace_clicked_method(class_name, method_sig)

    def trace_clicked_method(self, class_name, method_sig):
        """Start Frida tracing for the clicked method"""
        try:
            if self.Applist.currentIndex() < 0:
                return
                
            app_name = self.Applist.currentText()
            device_name = self.device_list.currentText()
            
            if device_name == "Select device":
                return
            
            # Get PID
            pid = self.get_pid_for_app(app_name, device_name)
            if not pid:
                return
            
            # Parse method name correctly from signature
            # method_sig example: "public void com.ansangha.drdriving.i.loadFromJson(java.lang.String)"
            # We need to extract just "loadFromJson"
            
            # Method 1: Extract after the last dot before '('
            if '.' in method_sig and '(' in method_sig:
                # Get everything before '('
                before_paren = method_sig.split('(')[0]
                # Split by dots and take the last part
                parts = before_paren.split('.')
                simple_method_name = parts[-1]  # This should be "loadFromJson"
                
                # But we need to check if the last part might be a return type like "void"
                # Clean it up - remove any access modifiers or return types
                access_modifiers = ['public', 'private', 'protected', 'static', 'final', 
                                   'synchronized', 'abstract', 'native', 'strictfp']
                return_types = ['void', 'boolean', 'byte', 'char', 'short', 'int', 
                               'long', 'float', 'double', 'String', 'Object']
                
                # If simple_method_name is in access modifiers or return types, 
                # then we need to look further back
                if simple_method_name in access_modifiers or simple_method_name in return_types:
                    # Take the second-to-last part
                    simple_method_name = parts[-2] if len(parts) >= 2 else simple_method_name
            else:
                # Fallback to old method
                simple_method_name = method_sig.split('(')[0]
            
            print(f"DEBUG: Class: {class_name}, Method sig: {method_sig}, Simple name: {simple_method_name}")
            
            # Create JS to trace this method - FIXED VERSION
            js_code = f"""'use strict';

Java.perform(function () {{
    var targetClass = "{class_name}";
    var targetMethodSig = "{method_sig}";
    var simpleMethodName = "{simple_method_name}";
    
    console.log("[*] Starting trace for: " + targetClass + "." + simpleMethodName);
    console.log("[*] Full signature: " + targetMethodSig);
    
    try {{
        var hook = Java.use(targetClass);
        
        // Check if the method exists in the class
        console.log("[*] Available methods in " + targetClass + ":");
        var methods = hook.class.getDeclaredMethods();
        var found = false;
        for (var i = 0; i < methods.length; i++) {{
            var methodStr = methods[i].toString();
            console.log("    " + methodStr);
            if (methodStr.includes(simpleMethodName + "(")) {{
                found = true;
            }}
        }}
        
        if (!found) {{
            console.log("[!] WARNING: Method " + simpleMethodName + " not found in class!");
        }}
        
        // Improved hook with better error handling
        hook[simpleMethodName].implementation = function() {{
            try {{
                console.log("[+] Method called: " + targetClass + "." + simpleMethodName);
                
                // Log arguments if any
                if (arguments.length > 0) {{
                    console.log("[+] Arguments (" + arguments.length + "):");
                    for (var i = 0; i < arguments.length; i++) {{
                        try {{
                            var arg = arguments[i];
                            if (arg === null) {{
                                console.log("    arg[" + i + "]: null");
                            }} else if (arg === undefined) {{
                                console.log("    arg[" + i + "]: undefined");
                            }} else if (typeof arg === 'string') {{
                                console.log("    arg[" + i + "]: \\"" + arg + "\\"");
                            }} else {{
                                console.log("    arg[" + i + "]: " + arg);
                                // For Java objects, try to call toString()
                                if (arg && arg.getClass) {{
                                    try {{
                                        console.log("    arg[" + i + "].toString(): " + arg.toString());
                                    }} catch (e) {{}}
                                }}
                            }}
                        }} catch (e) {{
                            console.log("    arg[" + i + "]: [Error displaying: " + e + "]");
                        }}
                    }}
                }} else {{
                    console.log("[+] No arguments");
                }}
                
                // Call original method
                var result = this[simpleMethodName].apply(this, arguments);
                
                // Check if method returns void
                var isVoid = targetMethodSig.includes(')V') || targetMethodSig.includes(' void ');
                
                // Log return value (if not void)
                if (!isVoid) {{
                    try {{
                        if (result === null || result === undefined) {{
                            console.log("[+] Method returned: null/undefined");
                        }} else if (result.getClass) {{
                            // It's a Java object
                            console.log("[+] Method returned Java object: " + result);
                            try {{
                                console.log("[+] Return toString(): " + result.toString());
                            }} catch (e) {{
                                console.log("[+] Could not call toString(): " + e);
                            }}
                        }} else {{
                            console.log("[+] Method returned primitive: " + result);
                        }}
                    }} catch (e) {{
                        console.log("[+] Could not log return value: " + e);
                    }}
                }} else {{
                    console.log("[+] Method completed (void)");
                }}
                
                return result;
                
            }} catch (e) {{
                console.log("[!] Exception in method: " + e);
                console.log("[!] Stack trace: " + e.stack);
                throw e;  // Re-throw to maintain original behavior
            }}
        }};
        
        console.log("[*] Hook installed successfully on " + simpleMethodName);
        
    }} catch (e) {{
        console.log("[!] Error setting up hook: " + e);
        console.log("[!] Stack trace: " + e.stack);
    }}
}});
"""
            
            # Save to file
            with open("trace_method.js", "w") as f:
                f.write(js_code)
            
            # Stop any existing tracing
            if self.frida_process:
                self.stop_frida_process()
            
            # Start Frida
            cmd = ["frida", "-U", "-p", str(pid), "-l", "trace_method.js"]
            self.is_monitoring = True
            self.frida_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Read output in thread
            threading.Thread(
                target=self.read_trace_output,
                args=(),
                daemon=True
            ).start()
            
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Error: {str(e)}")
    
    def read_trace_output(self):
        """Read trace output from Frida"""
        if not self.frida_process:
            return
        
        for line in self.frida_process.stdout:
            if not self.is_monitoring:
                break
            
            line = line.strip()
            if line:
                # Update Method Trace Console
                QtCore.QMetaObject.invokeMethod(
                    self.main_window,
                    "updateMethodTrace",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(str, line)
                )

    def get_class_methods(self, class_name, pid):
        """Get methods for a specific class"""
        try:
            # Stop any existing monitoring
            if self.frida_process:
                self.stop_frida_process()
            
            # Create JavaScript code to get methods for specific class
            js_code = f"""'use strict';

Java.perform(function () {{
    try {{
        var targetClass = "{class_name}";
        console.log("[*] Loading methods for class: " + targetClass);
        
        var clazz = Java.use(targetClass);
        var methods;
        
        try {{
            methods = clazz.class.getDeclaredMethods();
            console.log("[*] Using getdeclaredMethods()");
        }} catch (e) {{
            methods = clazz.class.getDeclaredMethods();
            console.log("[*] Using getDeclaredMethods()");
        }}
        
        console.log("[*] Found " + methods.length + " methods");
        
        for (var i = 0; i < methods.length; i++) {{
            var methodSig = methods[i].toString();
            // Extract just the method signature without the class name
            var methodOnly = methodSig;
            if (methodSig.startsWith(targetClass + ".")) {{
                methodOnly = methodSig.substring(targetClass.length + 1);
            }}
            console.log(targetClass + " -> " + methodOnly);
        }}
        
        console.log("[*] Done enumerating methods for " + targetClass);
    }} catch (e) {{
        console.log("Error accessing class: " + e);
    }}
}});
"""
            
            # Write to a temp file
            with open("single_class.js", "w") as f:
                f.write(js_code)
            
            # Run frida command
            cmd = [
                "frida",
                "-U",
                "-p", str(pid),
                "-l", "single_class.js"
            ]
            
            # Start frida process
            self.is_monitoring = True
            self.frida_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            method_count = 0
            lines_to_skip = 15  # Skip banner lines
            
            for i, line in enumerate(self.frida_process.stdout):
                if not self.is_monitoring:
                    break
                    
                line = line.strip()
                if not line:
                    continue
                
                # Skip banner lines
                if i < lines_to_skip:
                    if any(banner_text in line for banner_text in [
                        "____", "Frida", "Connected", "Attached", "Spawned", 
                        "Instrumenting", "  /  ", " |_| ", "     "
                    ]):
                        continue
                
                # Update console
                QtCore.QMetaObject.invokeMethod(
                    self.main_window,
                    "updateConsole",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(str, line)
                )
                
                # Parse method output
                if " -> " in line and class_name in line:
                    try:
                        # Format: "com.package.ClassName -> methodSignature"
                        parts = line.split(" -> ", 1)
                        if len(parts) == 2:
                            cls, method = parts
                            
                            # Add to listView in main thread
                            QtCore.QMetaObject.invokeMethod(
                                self.main_window,
                                "addMethodToList",
                                QtCore.Qt.QueuedConnection,
                                QtCore.Q_ARG(str, cls),
                                QtCore.Q_ARG(str, method)
                            )
                            
                            method_count += 1
                            
                            # Update status periodically
                            if method_count % 5 == 0:
                                QtCore.QMetaObject.invokeMethod(
                                    self.main_window,
                                    "updateStatusLabel",
                                    QtCore.Qt.QueuedConnection,
                                    QtCore.Q_ARG(str, f"Found {method_count} methods for {class_name}")
                                )
                    except Exception as e:
                        continue
            
            # Final update
            QtCore.QMetaObject.invokeMethod(
                self.main_window,
                "updateStatusLabel",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(str, f"Found {method_count} methods for {class_name}")
            )
            
            # Clean up
            self.is_monitoring = False
            self.frida_process = None
            
        except Exception as e:
            QtCore.QMetaObject.invokeMethod(
                self.main_window,
                "updateStatusLabel",
                QtCore.Qt.QueuedConnection,
                QtCore.Q_ARG(str, f"Error getting class methods: {str(e)}")
            )

    def init_method_tree(self):
        # Create the model and attach it to the listView widget.
        self.methodModel = QtGui.QStandardItemModel()
        self.methodModel.setHorizontalHeaderLabels(["Classes / Methods"])
        self.listView.setModel(self.methodModel)
    
    def list_classes_exact(self):
        """List classes EXACTLY like the example code - using file reading and simple approach"""
        try:
            # Stop any existing monitoring
            if self.frida_process:
                self.stop_frida_process()
            
            # Get selected app name
            if self.Applist.currentIndex() < 0 or self.Applist.currentText() == "Click Connect":
                self.status_label.setText("Please select an app first")
                return
            
            app_name = self.Applist.currentText()
            device_name = self.device_list.currentText()
            
            if device_name == "Select device":
                self.status_label.setText("Please select a device first")
                return
            
            # Clear previous classes
            self.comboBox.clear()
            self.classes_set.clear()
            
            # Get PID using frida-python
            pid = self.get_pid_for_app(app_name, device_name)
            if not pid:
                self.status_label.setText(f"Could not find PID for {app_name}. Make sure app is running.")
                return
            
            # Get package name
            package_name = self.get_package_for_app(app_name, device_name)
            if not package_name:
                self.status_label.setText(f"Could not get package name for {app_name}")
                return
            
            self.status_label.setText(f"Starting class enumeration for {app_name} (PID: {pid})...")
            
            # Save the JS code to class.js file
            js_code = """'use strict';

var TARGET = "__TARGET__";

function waitForJava() {
    if (!Java.available) {
        setTimeout(waitForJava, 100);
        return;
    }

    Java.perform(function () {
        var seen = {};

        function printClass(name) {
            if (!seen[name]) {
                seen[name] = true;
                console.log(name);
            }
        }

        Java.enumerateLoadedClasses({
            onMatch: function (name) {
                if (name.startsWith(TARGET)) {
                    printClass(name);
                }
            },
            onComplete: function () {}
        });

        var ClassLoader = Java.use("java.lang.ClassLoader");
        ClassLoader.loadClass.overload('java.lang.String').implementation = function (name) {
            var ret = this.loadClass(name);
            if (name.startsWith(TARGET)) {
                printClass(name);
            }
            return ret;
        };
    });
}

waitForJava();
"""
            
            # Replace the target placeholder
            js_code = js_code.replace("__TARGET__", package_name)
            
            # Write to class.js file
            with open("class.js", "w") as f:
                f.write(js_code)
            
            # Write to class_runtime.js with target replaced
            js_runtime = js_code  # Already has target replaced
            with open("class_runtime.js", "w") as f:
                f.write(js_runtime)
            
            # Build the frida command - EXACTLY like the example
            cmd = [
                "frida",
                "-U",
                "-p", pid,
                "-l", "class_runtime.js"
            ]
            
            # Start frida process - EXACTLY like the example
            self.is_monitoring = True
            self.frida_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Start reading output in background thread - EXACTLY like the example
            self.read_thread = threading.Thread(target=self.read_frida_output_exact, 
                                               args=(package_name,), 
                                               daemon=True)
            self.read_thread.start()
            
            self.status_label.setText(f"Enumerating classes for {package_name}...")
            
        except Exception as e:
            self.status_label.setText(f"Error starting class enumeration: {str(e)}")

    def read_frida_output_exact(self, package_name):
        """Read output from frida process EXACTLY like the example - IMPROVED BANNER FILTERING"""
        try:
            if not self.frida_process:
                return
            
            lines_to_skip = 15  # Skip approximately 15 lines of banner
            
            for i, line in enumerate(self.frida_process.stdout):
                if not self.is_monitoring:
                    break
                    
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Skip banner lines (first ~15 lines)
                if i < lines_to_skip:
                    # Check if this line is part of the banner
                    if any(banner_text in line for banner_text in [
                        "____", "Frida", "Connected", "Attached", "Spawned", 
                        "Instrumenting", "  /  ", " |_| ", "     "
                    ]):
                        continue
                
                # Update console in main thread using thread-safe method
                self.update_console_thread_safe(line)
                
                # ONLY real class names that start with the package - EXACTLY like the example
                if line.startswith(package_name):
                    if line not in self.classes_set:
                        self.classes_set.add(line)
                        
                        # Add to combobox in main thread using thread-safe method
                        self.add_class_thread_safe(line)
                        
                        # Update status with count
                        count = len(self.classes_set)
                        if count % 10 == 0:
                            self.update_status_thread_safe(f"Found {count} classes...")
            
            # Final update
            self.update_status_thread_safe(f"Found {len(self.classes_set)} classes total")
            
        except Exception as e:
            self.update_status_thread_safe(f"Error reading output: {str(e)}")

    def add_class_thread_safe(self, class_name):
        """Thread-safe method to add class to combobox"""
        QtCore.QMetaObject.invokeMethod(
            self.main_window,
            "addClassToComboBox",
            QtCore.Qt.QueuedConnection,
            QtCore.Q_ARG(str, class_name)
        )

    def update_status_thread_safe(self, text):
        """Thread-safe method to update status label"""
        QtCore.QMetaObject.invokeMethod(
            self.main_window,
            "updateStatusLabel",
            QtCore.Qt.QueuedConnection,
            QtCore.Q_ARG(str, text)
        )

    def update_console_thread_safe(self, text):
        """Thread-safe method to update console"""
        QtCore.QMetaObject.invokeMethod(
            self.main_window,
            "updateConsole",
            QtCore.Qt.QueuedConnection,
            QtCore.Q_ARG(str, text)
        )

    def get_pid_for_app(self, app_name, device_name):
        """Get PID for the selected app using frida-python bindings"""
        try:
            devices = frida.enumerate_devices()
            for dev in devices:
                if dev.name == device_name and dev.type == "usb":
                    apps = dev.enumerate_applications(scope='full')
                    for app in apps:
                        if app.name == app_name:
                            return str(app.pid)
                    break
            return None
        except:
            return None

    def get_package_for_app(self, app_name, device_name):
        """Get package name for the selected app using frida-python bindings"""
        try:
            devices = frida.enumerate_devices()
            for dev in devices:
                if dev.name == device_name and dev.type == "usb":
                    apps = dev.enumerate_applications(scope='full')
                    for app in apps:
                        if app.name == app_name:
                            # Try to get identifier (package name)
                            if hasattr(app, 'identifier'):
                                return app.identifier
                            # If not available, try to extract from parameters
                            if hasattr(app, 'parameters'):
                                if 'identifier' in app.parameters:
                                    return app.parameters['identifier']
                    break
            return None
        except:
            return None

    def stop_frida_process(self):
        """Stop the frida monitoring process"""
        self.is_monitoring = False
        if self.frida_process:
            try:
                self.frida_process.terminate()
                self.frida_process.wait(timeout=2)
            except:
                try:
                    self.frida_process.kill()
                except:
                    pass
            finally:
                self.frida_process = None

    def closeEvent(self, event):
        """Clean up when window is closed"""
        self.stop_frida_process()
        event.accept()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    @QtCore.pyqtSlot(str)
    def addClassToComboBox(self, class_name):
        """Slot to add class to combobox - called from thread"""
        self.ui.comboBox.addItem(class_name)
    
    @QtCore.pyqtSlot(str)
    def updateStatusLabel(self, text):
        """Slot to update status label - called from thread"""
        self.ui.status_label.setText(text)
    
    @QtCore.pyqtSlot(str)
    def updateConsole(self, text):
        """Slot to update console - called from thread"""
        self.ui.plainTextEdit_2.appendPlainText(text + "\n")

    @QtCore.pyqtSlot(str, str)
    def addMethodToList(self, class_name, method_sig):
        """Slot to add method to listView - called from thread"""
        # Create a formatted string for the method
        method_text = f"{class_name}\n  {method_sig}"
        
        # Create a QStandardItem with the method text
        item = QtGui.QStandardItem(method_text)
        item.setEditable(False)
        
        # Add to the model
        self.ui.methodModel.appendRow(item)
        
        # Scroll to the bottom to show newest items
        self.ui.listView.scrollToBottom()

    @QtCore.pyqtSlot(str)
    def updateMethodTrace(self, text):
        """Slot to update Method Trace Console"""
        self.ui.plainTextEdit.appendPlainText(text + "\n")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
