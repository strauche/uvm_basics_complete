// Filename: uvm_basics_complete.sv

//----------------------------------------------------------------------
//  Copyright (c) 2013 by Mentor Graphics Corp.
//  Copyright (c) 2011-2012 by Doulos Ltd.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
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

`include "uvm_macros.svh"

module dut(dut_if _if);

  import uvm_pkg::*;

  always @(posedge _if.clock)
  begin
    `uvm_info("mg", $psprintf("DUT received cmd=%b, addr=%d, data=%d",
                               _if.cmd, _if.addr, _if.data), UVM_NONE);
  end

endmodule: dut
