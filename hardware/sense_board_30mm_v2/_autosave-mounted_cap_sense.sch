(kicad_sch 
  (version 20250114) 
  (generator "eeschema") 
  (generator_version "9.0") 
  (uuid "77d8b71f-e4e8-4284-bc30-b01998247625") 
  (paper "A4") 
  (lib_symbols 
    (symbol "Connector:Conn_Coaxial" 
      (pin_names 
        (offset 1.016) 
        (hide yes)) 
      (exclude_from_sim no) 
      (in_bom yes) 
      (on_board yes) 
      (property "Reference" "J" 
        (at 0.254 3.048 0) 
        (effects 
          (font 
            (size 1.27 1.27)))) 
      (property "Value" "Conn_Coaxial" 
        (at 2.921 0 90) 
        (effects 
          (font 
            (size 1.27 1.27)))) 
      (property "Footprint" "" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "Datasheet" "~" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "Description" "coaxial connector (BNC, SMA, SMB, SMC, Cinch/RCA, LEMO, ...)" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "ki_keywords" "BNC SMA SMB SMC LEMO coaxial connector CINCH RCA MCX MMCX U.FL UMRF" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "ki_fp_filters" "*BNC* *SMA* *SMB* *SMC* *Cinch* *LEMO* *UMRF* *MCX* *U.FL*" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (symbol "Conn_Coaxial_0_1" 
        (polyline 
          (pts 
            (xy -2.54 0) 
            (xy -0.508 0)) 
          (stroke 
            (width 0) 
            (type default)) 
          (fill 
            (type none))) 
        (arc 
          (start 1.778 0) 
          (mid 0.222 -1.8079) 
          (end -1.778 -0.508) 
          (stroke 
            (width 0.254) 
            (type default)) 
          (fill 
            (type none))) 
        (arc 
          (start -1.778 0.508) 
          (mid 0.2221 1.8084) 
          (end 1.778 0) 
          (stroke 
            (width 0.254) 
            (type default)) 
          (fill 
            (type none))) 
        (circle 
          (center 0 0) 
          (radius 0.508) 
          (stroke 
            (width 0.2032) 
            (type default)) 
          (fill 
            (type none))) 
        (polyline 
          (pts 
            (xy 0 -2.54) 
            (xy 0 -1.778)) 
          (stroke 
            (width 0) 
            (type default)) 
          (fill 
            (type none)))) 
      (symbol "Conn_Coaxial_1_1" 
        (pin passive line 
          (at -5.08 0 0) 
          (length 2.54) 
          (name "In" 
            (effects 
              (font 
                (size 1.27 1.27)))) 
          (number "1" 
            (effects 
              (font 
                (size 1.27 1.27))))) 
        (pin passive line 
          (at 0 -5.08 90) 
          (length 2.54) 
          (name "Ext" 
            (effects 
              (font 
                (size 1.27 1.27)))) 
          (number "2" 
            (effects 
              (font 
                (size 1.27 1.27)))))) 
      (embedded_fonts no)) 
    (symbol "power:GND" 
      (power) 
      (pin_numbers 
        (hide yes)) 
      (pin_names 
        (offset 0) 
        (hide yes)) 
      (exclude_from_sim no) 
      (in_bom yes) 
      (on_board yes) 
      (property "Reference" "#PWR" 
        (at 0 -6.35 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "Value" "GND" 
        (at 0 -3.81 0) 
        (effects 
          (font 
            (size 1.27 1.27)))) 
      (property "Footprint" "" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "Datasheet" "" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "Description" "Power symbol creates a global label with name \"GND\" , ground" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (property "ki_keywords" "global power" 
        (at 0 0 0) 
        (effects 
          (font 
            (size 1.27 1.27)) 
          (hide yes))) 
      (symbol "GND_0_1" 
        (polyline 
          (pts 
            (xy 0 0) 
            (xy 0 -1.27) 
            (xy 1.27 -1.27) 
            (xy 0 -2.54) 
            (xy -1.27 -1.27) 
            (xy 0 -1.27)) 
          (stroke 
            (width 0) 
            (type default)) 
          (fill 
            (type none)))) 
      (symbol "GND_1_1" 
        (pin power_in line 
          (at 0 0 270) 
          (length 0) 
          (name "~" 
            (effects 
              (font 
                (size 1.27 1.27)))) 
          (number "1" 
            (effects 
              (font 
                (size 1.27 1.27)))))) 
      (embedded_fonts no))) 
  (junction 
    (at 69.84999999999999 95.25) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "22c34589-3677-467f-94f7-7fcb06f1d4e4")) 
  (junction 
    (at 69.84999999999999 121.92) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "4df64297-6919-44f7-bb71-c1e09a374cbe")) 
  (junction 
    (at 69.84999999999999 113.03) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "578384c1-4151-4471-9bb7-5db0bd7cfd5e")) 
  (junction 
    (at 69.84999999999999 86.36) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "57e196b0-544b-4725-a819-ad846ded05fc")) 
  (junction 
    (at 69.84999999999999 77.47) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "87f653a0-4da3-4b62-95a0-b58f8ca3cb87")) 
  (junction 
    (at 69.84999999999999 104.14) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "9d85d8d1-d626-49c5-8f80-7fff88c12801")) 
  (junction 
    (at 69.84999999999999 68.58) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "da82f494-3409-4b55-8569-1ae8ec9f2018")) 
  (junction 
    (at 69.84999999999999 59.69) 
    (diameter 0) 
    (color 0 0 0 0) 
    (uuid "edd2bd0c-8a46-4e78-8b4e-9e7e2636003e")) 
  (wire 
    (pts 
      (xy 52.07 77.47) 
      (xy 69.84999999999999 77.47)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "078c6c1b-eb4b-4486-93c7-becc1d189811")) 
  (wire 
    (pts 
      (xy 69.84999999999999 77.47) 
      (xy 69.84999999999999 86.36)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "20ba524e-e307-4496-a0f5-051d1e8bc3b1")) 
  (wire 
    (pts 
      (xy 69.84999999999999 59.69) 
      (xy 69.84999999999999 68.58)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "24dccf24-4fc8-40e0-aee3-ebec57427792")) 
  (wire 
    (pts 
      (xy 52.07 121.92) 
      (xy 69.84999999999999 121.92)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "2f0fb20c-2cb3-448f-8560-61590ff1ab39")) 
  (wire 
    (pts 
      (xy 69.84999999999999 86.36) 
      (xy 69.84999999999999 95.25)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "4bcbdd47-9ba4-4c26-868a-4581fe23680d")) 
  (wire 
    (pts 
      (xy 69.84999999999999 50.8) 
      (xy 52.07 50.8)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "4ea5494c-695e-42a1-a508-40c6973f10dd")) 
  (wire 
    (pts 
      (xy 52.07 86.36) 
      (xy 69.84999999999999 86.36)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "50fdd6db-f524-43e5-88ae-9fd66a3f41c5")) 
  (wire 
    (pts 
      (xy 69.84999999999999 104.14) 
      (xy 69.84999999999999 113.03)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "6d8380cd-90a6-4bc5-a498-0eef29dba710")) 
  (wire 
    (pts 
      (xy 69.84999999999999 95.25) 
      (xy 69.84999999999999 104.14)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "7cf7708b-e4f0-400d-a634-a7812259a081")) 
  (wire 
    (pts 
      (xy 52.07 104.14) 
      (xy 69.84999999999999 104.14)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "89330020-ac77-4a93-af2b-e8fa86de12a0")) 
  (wire 
    (pts 
      (xy 52.07 95.25) 
      (xy 69.84999999999999 95.25)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "a9e0c326-b40a-45a6-a0a8-b7550f7a9a21")) 
  (wire 
    (pts 
      (xy 69.84999999999999 68.58) 
      (xy 69.84999999999999 77.47)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "c761ddf1-c8d4-4973-92f1-2d4c1bdd89b8")) 
  (wire 
    (pts 
      (xy 69.84999999999999 113.03) 
      (xy 69.84999999999999 121.92)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "cb594587-991f-4091-b2dc-7b640502d50b")) 
  (wire 
    (pts 
      (xy 52.07 59.69) 
      (xy 69.84999999999999 59.69)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "dca5f2b3-a3eb-4ece-b4b1-ce0e4798aa2c")) 
  (wire 
    (pts 
      (xy 69.84999999999999 50.8) 
      (xy 69.84999999999999 59.69)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "de937930-8b3c-4eac-9e86-29e577c41a80")) 
  (wire 
    (pts 
      (xy 52.07 113.03) 
      (xy 69.84999999999999 113.03)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "e7bdc0ca-730d-4055-a41e-765a5ee20b6e")) 
  (wire 
    (pts 
      (xy 52.07 68.58) 
      (xy 69.84999999999999 68.58)) 
    (stroke 
      (width 0) 
      (type default)) 
    (uuid "faeedeac-6ea1-4bfa-99ed-dabd51be306e")) 
  (label "5" 
    (at 46.99 81.28 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "0aa7bb08-16f1-48be-9dd9-3a1fe848fc4c")) 
  (label "8" 
    (at 46.99 107.95 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "2ad401ff-d2c6-4dcd-b3a2-dcdd8570ab1c")) 
  (label "1" 
    (at 46.99 45.72 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "2cbea9c3-1e1f-488f-9cf2-b4d4c85593dd")) 
  (label "2" 
    (at 46.99 54.61 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "3f6ad332-700c-4ddf-85b6-6fbf1d5e691b")) 
  (label "4" 
    (at 46.99 72.39 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "76fa66db-ce19-4a88-b308-59ae012149ba")) 
  (label "6" 
    (at 46.99 90.17 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "9bb5ad29-2848-400c-b2b7-66d50e3928eb")) 
  (label "R" 
    (at 46.99 116.84 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "a9942596-a2af-4b81-b447-69f9dc961710")) 
  (label "3" 
    (at 46.99 63.5 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "aac8c8f6-ea57-442c-b445-e05a26ee9338")) 
  (label "7" 
    (at 46.99 99.06 0) 
    (effects 
      (font 
        (size 1.27 1.27)) 
      (justify left bottom)) 
    (uuid "e007b845-7a3b-4e2c-9aee-51d8ac6ee973")) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 45.72 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-000068019e44") 
    (property "Reference" "J1" 
      (at 54.61 46.355 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 48.6664 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 45.72 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 45.72 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 45.72 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "5b55fabe-e3fc-4166-ac27-ae05fe1cf0f9")) 
    (pin "2" 
      (uuid "89487d63-e2c2-4ebd-9e1c-9227a05bb4da")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J1") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 54.61 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-00006802b178") 
    (property "Reference" "J2" 
      (at 54.61 55.245 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 57.5564 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 54.61 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 54.61 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 54.61 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "5b256ce9-4cad-417d-b421-a0214c645750")) 
    (pin "2" 
      (uuid "fd7ef69f-48f8-4540-9377-97d984f13271")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J2") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 63.5 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-00006802ba9a") 
    (property "Reference" "J3" 
      (at 54.61 64.13500000000001 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 66.4464 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 63.5 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 63.5 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 63.5 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "1d829805-0537-45f3-9aea-fa54c71883a8")) 
    (pin "2" 
      (uuid "9f036631-d680-478b-81ee-5c3e1d88deda")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J3") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 72.39 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-00006802bf72") 
    (property "Reference" "J4" 
      (at 54.61 73.02500000000001 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 75.3364 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 72.39 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 72.39 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 72.39 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "8c6fd8cd-5ce0-40fd-b992-fa7969ee7827")) 
    (pin "2" 
      (uuid "2bacabb2-b20f-4b8d-9468-a03d85665b28")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J4") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 81.28 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-00006802c33e") 
    (property "Reference" "J5" 
      (at 54.61 81.91500000000001 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 84.2264 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 81.28 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 81.28 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 81.28 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "2" 
      (uuid "62092eca-4c55-45ad-abeb-d61d7e47b52c")) 
    (pin "1" 
      (uuid "37dcbaef-376b-4593-9cc5-2746e5683d85")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J5") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 90.17 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-000068034970") 
    (property "Reference" "J6" 
      (at 54.61 90.80500000000001 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 93.1164 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 90.17 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 90.17 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 90.17 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "2" 
      (uuid "953e1c43-f8e0-45c2-addc-a064da7081f9")) 
    (pin "1" 
      (uuid "e7fb20d0-a72d-4cf7-9054-aab18c694906")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J6") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 99.06 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-000068034976") 
    (property "Reference" "J7" 
      (at 54.61 99.69499999999999 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 102.0064 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 99.06 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 99.06 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 99.06 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "2" 
      (uuid "749f3cd9-0b80-45b0-897f-d9bca61f5402")) 
    (pin "1" 
      (uuid "367c7853-0bf1-4950-964d-439caed8d8b8")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J7") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 107.95 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-00006803497c") 
    (property "Reference" "J8" 
      (at 54.61 108.585 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 110.8964 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 107.95 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 107.95 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 107.95 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "2" 
      (uuid "899f4042-b7ae-408d-a92d-7b6611f32a88")) 
    (pin "1" 
      (uuid "1f4fb08a-d09f-41c3-9fd8-114501e535da")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "J8") 
          (unit 1))))) 
  (symbol 
    (lib_id "Connector:Conn_Coaxial") 
    (at 52.07 116.84 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-000068034982") 
    (property "Reference" "JT1" 
      (at 54.61 117.475 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Value" "Conn_Coaxial" 
      (at 54.61 119.7864 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (justify left))) 
    (property "Footprint" "Connector_Coaxial:MMCX_Molex_73415-1471_Vertical" 
      (at 52.07 116.84 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "~" 
      (at 52.07 116.84 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 52.07 116.84 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "75c0d9a5-c5db-435a-a17e-7434a64abf14")) 
    (pin "2" 
      (uuid "25fece4b-b4e5-4ff8-870d-d7f5e12c12f8")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "JT1") 
          (unit 1))))) 
  (symbol 
    (lib_id "power:GND") 
    (at 69.84999999999999 121.92 0) 
    (unit 1) 
    (exclude_from_sim no) 
    (in_bom yes) 
    (on_board yes) 
    (dnp no) 
    (uuid "00000000-0000-0000-0000-000068035149") 
    (property "Reference" "#PWR0101" 
      (at 69.84999999999999 128.27 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Value" "GND" 
      (at 69.977 126.3142 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (property "Footprint" "" 
      (at 69.84999999999999 121.92 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Datasheet" "" 
      (at 69.84999999999999 121.92 0) 
      (effects 
        (font 
          (size 1.27 1.27)) 
        (hide yes))) 
    (property "Description" "" 
      (at 69.84999999999999 121.92 0) 
      (effects 
        (font 
          (size 1.27 1.27)))) 
    (pin "1" 
      (uuid "f7084f64-7978-48be-8d9d-aefcda304708")) 
    (instances 
      (project "" 
        (path "/77d8b71f-e4e8-4284-bc30-b01998247625" 
          (reference "#PWR0101") 
          (unit 1))))) 
  (sheet_instances 
    (path "/" 
      (page "1"))) 
  (embedded_fonts no))