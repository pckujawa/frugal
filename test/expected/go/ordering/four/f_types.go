// Autogenerated by Frugal Compiler (2.8.0)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

package four

import (
	"bytes"
	"fmt"

	"git.apache.org/thrift.git/lib/go/thrift"
)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = bytes.Equal

var GoUnusedProtection__ int

func init() {
}

type Four struct {
	SomeField []bool `thrift:"some_field,1" db:"some_field" json:"some_field"`
}

func NewFour() *Four {
	return &Four{}
}

func (p *Four) GetSomeField() []bool {
	return p.SomeField
}

func (p *Four) Read(iprot thrift.TProtocol) error {
	if _, err := iprot.ReadStructBegin(); err != nil {
		return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
	}

	for {
		_, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
		if err != nil {
			return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
		}
		if fieldTypeId == thrift.STOP {
			break
		}
		switch fieldId {
		case 1:
			if err := p.ReadField1(iprot); err != nil {
				return err
			}
		default:
			if err := iprot.Skip(fieldTypeId); err != nil {
				return err
			}
		}
		if err := iprot.ReadFieldEnd(); err != nil {
			return err
		}
	}
	if err := iprot.ReadStructEnd(); err != nil {
		return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", p), err)
	}
	return nil
}

func (p *Four) ReadField1(iprot thrift.TProtocol) error {
	_, size, err := iprot.ReadListBegin()
	if err != nil {
		return thrift.PrependError("error reading list begin: ", err)
	}
	p.SomeField = make([]bool, 0, size)
	for i := 0; i < size; i++ {
		var elem1 bool
		if v, err := iprot.ReadBool(); err != nil {
			return thrift.PrependError("error reading field 0: ", err)
		} else {
			elem1 = v
		}
		p.SomeField = append(p.SomeField, elem1)
	}
	if err := iprot.ReadListEnd(); err != nil {
		return thrift.PrependError("error reading list end: ", err)
	}
	return nil
}

func (p *Four) Write(oprot thrift.TProtocol) error {
	if err := oprot.WriteStructBegin("Four"); err != nil {
		return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err)
	}
	if err := p.writeField1(oprot); err != nil {
		return err
	}
	if err := oprot.WriteFieldStop(); err != nil {
		return thrift.PrependError("write field stop error: ", err)
	}
	if err := oprot.WriteStructEnd(); err != nil {
		return thrift.PrependError("write struct stop error: ", err)
	}
	return nil
}

func (p *Four) writeField1(oprot thrift.TProtocol) error {
	if err := oprot.WriteFieldBegin("some_field", thrift.LIST, 1); err != nil {
		return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:some_field: ", p), err)
	}
	if err := oprot.WriteListBegin(thrift.BOOL, len(p.SomeField)); err != nil {
		return thrift.PrependError("error writing list begin: ", err)
	}
	for _, v := range p.SomeField {
		if err := oprot.WriteBool(bool(v)); err != nil {
			return thrift.PrependError(fmt.Sprintf("%T. (0) field write error: ", p), err)
		}
	}
	if err := oprot.WriteListEnd(); err != nil {
		return thrift.PrependError("error writing list end: ", err)
	}
	if err := oprot.WriteFieldEnd(); err != nil {
		return thrift.PrependError(fmt.Sprintf("%T write field end error 1:some_field: ", p), err)
	}
	return nil
}

func (p *Four) String() string {
	if p == nil {
		return "<nil>"
	}
	return fmt.Sprintf("Four(%+v)", *p)
}
