// Filename: uvm_basics_complete.sv

//----------------------------------------------------------------------
//  Copyright (c) 2013 by Mentor Graphics Corp.
//  Copyright (c) 2011-2012 by Doulos Ltd.
//  Copyright (c) 2021 by Strauch Consulting, LLC
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//  http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//----------------------------------------------------------------------
// Source code example for Mentor Graphics Verification Academy UVM Basics Module
// Sessions 3-8
// Original Author: John Aynsley, Doulos
// Updated: Tom Fitzpatrick, Mentor Graphics
// Date:   10-Mar-2011
// Date:   19-Oct-2012  Updated for UVM 1.1 by replacing start_item(seq) with seq.start() 
// Date:   31-Jul-2013  Modified code to be consistent with UVM Cookbook
// Date:   29-Jun-2021  Break out code to multiple files. Remode interface from port list.

`include "uvm_macros.svh"

module dut (input wire clock, reset, cmd,
            input logic [7:0] addr, data);

  always @(posedge clock)
  begin
    $sformatf ("DUT received cmd=%b, addr=%d, data=%d", cmd, addr, data);
  end

endmodule: dut
